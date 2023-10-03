from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from perfin.config import DB_ECHO, DB_URL

# Create an engine
engine = create_engine(DB_URL, echo=DB_ECHO)

# Create a base class for the model
Base = declarative_base()

# Create a Session class
Session = sessionmaker(bind=engine)


def get_session():
    return Session()
