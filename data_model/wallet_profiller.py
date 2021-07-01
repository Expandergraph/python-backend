import enum

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class EthFlowTypeEnum(enum.Enum):
    incoming = 1
    outgoing = 2


class EthFlow(Base):
    __tablename__ = "eth_flow"

    id = Column(Integer, primary_key=True)
    type = Column(Enum(EthFlowTypeEnum))
    exchange = Column(String(64))
    volume = Column(Float)
    parent_id = Column(Integer, ForeignKey('address.id'))

    def __init__(self, type, exchange, volume, parent_id):
        self.type = type
        self.exchange = exchange
        self.volume = volume
        self.parent_id = parent_id
