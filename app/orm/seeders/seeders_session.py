from sqlalchemy.orm import sessionmaker

from orm.settings import engine

engine.echo = True
seeders_session = sessionmaker(bind=engine)
