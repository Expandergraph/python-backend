import enum

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from base import Base


class TokenSeniorityDistribution(Base):
    __tablename__ = "token_seniority_distribution"

    id = Column(Integer, primary_key=True)
    token = Column(String(64))
    pct_token_less_7d = Column(Integer)
    pct_token_7d_to_30d = Column(Integer)
    pct_address_less_7d = Column(Integer)
    pct_address_7d_to_30d = Column(Integer)

    def __init__(self, timestamp, token, pct_token_less_7d, pct_token_7d_to_30d, pct_address_less_7d,
                 pct_address_7d_to_30d):
        self.timestamp = timestamp
        self.token = token
        self.pct_token_less_7d = pct_token_less_7d
        self.pct_token_7d_to_30d = pct_token_7d_to_30d
        self.pct_address_less_7d = pct_address_less_7d
        self.pct_address_7d_to_30d = pct_address_7d_to_30d


class UniqueAddressesForToken(Base):
    __tablename__ = "unique_addresses_for_token"

    id = Column(Integer, primary_key=True)
    timestamp = Column(Date)
    token = Column(String(64))
    num_unique_addresses = Column(Integer)

    def __init__(self, timestamp, token, num_unique_addresses):
        self.timestamp = timestamp
        self.token = token
        self.num_unique_addresses = num_unique_addresses
