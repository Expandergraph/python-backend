import sys
sys.path.append("..")
from sqlalchemy.orm import relationship, sessionmaker

# from address_overview import *
# from top_labels import *
# from holders import *
# from notable_wallets import *
from token_exchanges_overview import *
# from top_balances import *
# from top_transactions import *
# from wallet_profiller import *

from base import engine, session

import datetime
sample_date = datetime.datetime(2020, 11, 30)

Base.metadata.create_all(engine)
# label = Label(name="NFT", address="0x829bd824b016326a401d083b33d092293333a832")
# session.add(label)
# balance = TokenBalance(token="ETH", address="0x829bd824b016326a401d083b33d092293333a832", balance=1.5)
# balance = TokenBalance(token="ECG", address="0x829bd824b016326a401d083b33d092293333a832", balance=2.5)
# session.add(balance)
# dailyactivity = DailyActivity(date=sample_date, address="0x829bd824b016326a401d083b33d092293333a832", transactions=50)
# # session.add(dailyactivity)

# counter_party = Counterparty(flow_type=EthFlowTypeEnum.incoming, exchange="OKEX", volume=324, address="0x829bd824b016326a401d083b33d092293333a832")
# counter_party = Counterparty(flow_type=EthFlowTypeEnum.incoming, exchange="Uniswap", volume=255, address="0x829bd824b016326a401d083b33d092293333a832")
# counter_party = Counterparty(flow_type=EthFlowTypeEnum.outgoing, exchange="Uniswap", volume=723, address="0x829bd824b016326a401d083b33d092293333a832")
# counter_party = Counterparty(flow_type=EthFlowTypeEnum.outgoing, exchange="Tokenlon", volume=55, address="0x829bd824b016326a401d083b33d092293333a832")
# session.add(counter_party)

# top_label = TopLabel(
# label = 'High Activity',
# transactions = 117,
# num_addresses=40,
# eth_vol=23,
# vol_out_eth=9.95,
# vol_in_eth=13,
# num_token_txs=62,
# txs_in_tokens=38,
# txs_out_tokens=24
# )
# session.add(top_label)

# supply_ratio = TokenExchangeSupplyRatio(token="GTC", ratio=0.0067)
# session.add(supply_ratio)

#token_txsnum = TokenBalancesComparison(token)

token_balances_comp = TokenBalancesComparison(token="GTC", pct_of_dex_traders=1, pct_of_exchanges=0, date=sample_date)
session.add(token_balances_comp)
session.commit()
session.close()

