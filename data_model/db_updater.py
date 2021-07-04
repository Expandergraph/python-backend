from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker

from address_overview import *
from top_labels import *
from holders import *
from notable_wallets import *
from token_exchanges_overview import *
from top_balances import *
from top_transactions import *
from wallet_profiller import *

USERNAME = ''
PASSWORD = ''
IP = ''
PORT = '3306'
DB = 'xpander'

engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{IP}:{PORT}/{DB}')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.commit()
session.close()

