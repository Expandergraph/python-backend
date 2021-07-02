import enum

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class TopBalances(Base):
    __tablename__ = "top_balances"