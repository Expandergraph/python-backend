import enum

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TopTransaction(Base):
    __tablename__ = "top_transactions"

    id = Column(Integer, primary_key=True)
    source = Column(String(64))
    destination = Column(String(64))
    volume = Column(Integer)
    days = Column(Integer)

    def __init__(self, source, destination, volume, days):
        self.source = source
        self.destination = destination
        self.volume = volume
        self.days = days
