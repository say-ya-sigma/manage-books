from orm.settings import engine
from sqlalchemy.orm import sessionmaker

engine.echo = True
seeders_session = sessionmaker(bind=engine)()
