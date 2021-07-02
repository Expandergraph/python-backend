import enum

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class TokenBalanceTypeEnum(enum.Enum):
    dex_traders = 1
    exchanges = 2


class TokenExchangeSupplyRatio(Base):
    __tablename__ = "token_exchange_supply_ratio"

    id = Column(Integer, primary_key=True)
    token = Column(String(64))
    ratio = Column(Float)

    def __init__(self, token, ratio):
        self.name = token
        self.ratio = ratio


class TokenBalancesComparison(Base):
    __tablename__ = "token_balances_comparison"

    id = Column(Integer, primary_key=True)
    token = Column(String(64))
    type = Column(Enum(TokenBalanceTypeEnum))
    pct_of_total_supply = Column(Float)

    def __init__(self, token, type, pct_of_total_supply):
        self.token = token
        self.type = type
        self.pct_of_total_supply = pct_of_total_supply


class TokensOnExchanges(Base):
    __tablename__ = "tokens_on_exchanges"

    id = Column(Integer, primary_key=True)
    token = Column(String(64))
    exchange = Column(String(64))
    date = Column(Date)
    volume = Column(Integer)

    def __init__(self, token, exchange, date, volume):
        self.token = token
        self.exchange = exchange
        self.date = date
        self.volume = volume


class TopExchange(Base):
    __tablename__ = "top_exchanges"

    id = Column(Integer, primary_key=True)
    token = Column(String(64))
    exchange = Column(String(64))
    balance = Column(Integer)
    change = Column(Integer)
    first_in = Column(Integer)

    def __init__(self, token, exchange, balance, change, first_in):
        self.token = token
        self.exchange = exchange
        self.balance = balance
        self.change = change
        self.first_in = first_in

engine = create_engine('')

Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
top_exchange = TopExchange(token='GTC', exchange='Binance', balance=100, change=50, first_in=20)
session.add(top_exchange)
session.commit()
session.close()