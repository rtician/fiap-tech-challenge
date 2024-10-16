from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URL)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
