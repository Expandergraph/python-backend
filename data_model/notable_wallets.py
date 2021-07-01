import enum

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class NotableWallets(Base):
    __tablename__ = "notable_wallets"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    change = Column(Integer)
    balance = Column(Integer)
    first_in = Column(Integer)
    depositors = Column(String(256))
    recipients = Column(String(256))

    def __init__(self, name, change, balance, first_in, depositors, recipients):
        self.name = name
        self.change = change
        self.balance = balance
        self.first_in = first_in
        self.depositors = depositors
        self.recipients = recipients
