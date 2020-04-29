from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:mypassword@localhost:5432/Travancore',echo=True)

Session = sessionmaker(bind = engine)

Base = declarative_base()

session = Session()

