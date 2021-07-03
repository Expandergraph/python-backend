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


engine = create_engine('')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.commit()
session.close()

