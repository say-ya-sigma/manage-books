from migrations.migrate_target import *  # noqa: F403
from orm.settings import engine
from sqlalchemy import Engine


def truncate_db(engine: Engine):
    meta = Base.metadata  # noqa: F405
    con = engine.connect()
    trans = con.begin()
    con.exec_driver_sql("SET CONSTRAINTS ALL DEFERRED;")
    for table in meta.sorted_tables:
        con.execute(table.delete())
    con.exec_driver_sql("SET CONSTRAINTS ALL IMMEDIATE;")
    trans.commit()

if __name__ == "__main__":
  truncate_db(engine)
