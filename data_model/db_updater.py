import sys
sys.path.append("..")
from sqlalchemy.orm import relationship, sessionmaker

from address_overview import *
from top_labels import *
from holders import *
from notable_wallets import *
from token_exchanges_overview import *
from top_balances import *
from top_transactions import *
from wallet_profiller import *

from base import engine

import datetime
sample_date = datetime.datetime(2020, 11, 30)

#Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
#label = Label(name="NFT", address="0x829bd824b016326a401d083b33d092293333a832")
#session.add(label)
# balance = TokenBalance(token="ETH", address="0x829bd824b016326a401d083b33d092293333a832", balance=1.5)
# balance = TokenBalance(token="ECG", address="0x829bd824b016326a401d083b33d092293333a832", balance=2.5)
# session.add(balance)
dailyactivity = DailyActivity(date=sample_date, address="0x829bd824b016326a401d083b33d092293333a832", transactions=50)
session.add(dailyactivity)
session.commit()
session.close()

