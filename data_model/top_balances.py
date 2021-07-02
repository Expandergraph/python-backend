import enum

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TokenSeniorityDistribution(Base):
    __tablename__ = "token_seniority_distribution"

    id = Column(Integer, primary_key=True)
    timestamp = Column(Date)
    pct_token_less_7d = Column(Integer)
    pct_token_7d_to_30d = Column(Integer)
    pct_address_less_7d = Column(Integer)
    pct_address_7d_to_30d = Column(Integer)

    def __init__(self, timestamp, pct_token_less_7d, pct_token_7d_to_30d, pct_address_less_7d, pct_address_7d_to_30d):
        self.timestamp = timestamp
        self.pct_token_less_7d = pct_token_less_7d
        self.pct_token_7d_to_30d = pct_token_7d_to_30d
        self.pct_address_less_7d = pct_address_less_7d
        self.pct_address_7d_to_30d = pct_address_7d_to_30d
