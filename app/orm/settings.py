from orm.mixins.TimestampMixin import TimestampMixin
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    QueryPropertyDescriptor,
    Session,
    scoped_session,
    sessionmaker,
)

# 接続先DBの設定
DATABASE = "postgresql://flask_user:flask_password@db:5432/flask_db"

engine = create_engine(DATABASE)

session = scoped_session(sessionmaker(bind=engine))


class Base(DeclarativeBase, TimestampMixin):
    session: scoped_session[Session]
    query: QueryPropertyDescriptor

Base.query = session.query_property()
Base.session = session
