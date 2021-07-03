import enum

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from base import Base


class EthFlowTypeEnum(enum.Enum):
    incoming = 1
    outgoing = 2


class Counterparties(Base):
    __tablename__ = "counterparties"

    id = Column(Integer, primary_key=True)
    flow_type = Column(Enum(EthFlowTypeEnum))
    exchange = Column(String(64))
    volume = Column(Float)
    address = Column(String(64))
    parent_id = Column(Integer, ForeignKey('address.id'))

    def __init__(self, flow_type, exchange, volume, parent_id):
        self.flow_type = flow_type
        self.exchange = exchange
        self.volume = volume
        self.parent_id = parent_id
