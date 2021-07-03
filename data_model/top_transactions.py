import enum
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from base import Base


class TopTransaction(Base):
    __tablename__ = "top_transactions"

    id = Column(Integer, primary_key=True)
    token = Column(String(64))
    source = Column(String(64))
    destination = Column(String(64))
    volume = Column(Integer)
    days = Column(Integer)

    def __init__(self, token, source, destination, volume, days):
        self.token = token
        self.source = source
        self.destination = destination
        self.volume = volume
        self.days = days
