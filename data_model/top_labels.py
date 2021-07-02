from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TopLabel(Base):
    __tablename__ = "top_labels"

    id = Column(Integer, primary_key=True)
    label = Column(String(64))
    transactions = Column(Integer)
    addresses = Column(Integer)
    vol_out_eth = Column(Float)
    vol_in_eth = Column(Float)
    txs_in_tokens = Column(Integer)
    txs_out_tokens = Column(Integer)

    def __init__(self, label, transactions, addresses, vol_out_eth, vol_in_eth, txs_in_tokens, txs_out_tokens):
        self.label = label
        self.transactions = transactions
        self.addresses = addresses
        self.vol_out_eth = vol_out_eth
        self.vol_in_eth = vol_in_eth
        self.txs_in_tokens = txs_in_tokens
        self.txs_out_tokens = txs_out_tokens
