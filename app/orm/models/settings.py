from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, DeclarativeBase, QueryPropertyDescriptor

# 接続先DBの設定
DATABASE = 'postgresql://flask_user:flask_password@db:5432/flask_db'

engine = create_engine(
  DATABASE
)

session = scoped_session(
  sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
  )
)

class Base(DeclarativeBase):
  query: QueryPropertyDescriptor
  def __init__(self):
    self.query = session.query_property()