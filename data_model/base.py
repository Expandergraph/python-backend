from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
USERNAME = 'myuser'
PASSWORD = 'mypass@bR2021'
IP = '107.182.26.178'
PORT = '3306'
DB = 'xpander'

engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{IP}:{PORT}/{DB}')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()
