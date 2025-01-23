import alembic.command
import alembic.config
import pytest
from orm.seeders.run import run as seeder_run
from orm.settings import Base
from presentation.route import wsgi
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database


class TestingSession(Session):
    def commit(self):
        self.flush()
        self.expire_all()


def migrate(
    migrations_path,
    db_url,
    alembic_ini_path="alembic.ini",
    connection=None,
    revision="head"
):
    config = alembic.config.Config(alembic_ini_path)
    config.set_main_option("sqlalchemy.url", db_url)
    config.set_main_option("script_location", migrations_path)
    if connection:
        config.attributes["connection"] = connection
    alembic.command.upgrade(config, revision)

@pytest.fixture(scope="function", autouse=True)
def rollback():
    yield
    Base.session.rollback()

@pytest.fixture(scope="session")
def client():
    test_url = "postgresql://flask_user:flask_password@db:5432/flask_test_db"

    # 既にテスト用データベースが存在していたら破棄する
    if database_exists(test_url):
        drop_database(test_url)

    # テスト用データベースを作成する
    create_database(test_url)

    engine = create_engine(test_url)

    with engine.begin() as connection:
        # マイグレーションを実行
        migrate("app/migrations",db_url=test_url, connection=connection)
    engine.dispose()

    session: scoped_session[Session] = scoped_session(
        sessionmaker(bind=engine, class_=TestingSession, expire_on_commit=False)
    )
    seeder_session = scoped_session(sessionmaker(bind=engine))
    Base.query = session.query_property()
    Base.session = session

    wsgi.config["TESTING"] = True

    with wsgi.test_client() as client:
        seeder_run(session=seeder_session())

        yield client

        drop_database(test_url)
