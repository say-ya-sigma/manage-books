from migrations.migrate_target import *  # noqa: F403
from orm.settings import engine
from sqlalchemy import Engine


def drop_all_db(engine: Engine):
    meta = Base.metadata  # noqa: F405
    meta.drop_all(engine)
    con = engine.connect()
    trans = con.begin()
    con.exec_driver_sql("DROP TABLE alembic_version;")
    trans.commit()

if __name__ == "__main__":
  drop_all_db(engine)
