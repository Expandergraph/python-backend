from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from wallet_profiller import Counterparties

from base import Base

class Label(Base):
    __tablename__ = "label"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

    def __init__(self, name):
        self.name = name


class TokenBalance(Base):
    __tablename__ = "token_balance"

    id = Column(Integer, primary_key=True)
    token = Column(String(64))
    balance = Column(Float)
    parent_id = Column(Integer, ForeignKey('address.id'))

    def __init__(self, token, balance, parent_id):
        self.token = token
        self.balance = balance
        self.parent_id = parent_id


class DailyActivity(Base):
    __tablename__ = "daily_activities"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    transactions = Column(Integer)
    parent_id = Column(Integer, ForeignKey('address.id'))

    def __init__(self, date, transactions, parent_id):
        self.date = date
        self.transactions = transactions
        self.parent_id = parent_id


class HourlyActivity(Base):
    __tablename__ = "hourly_activities"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    transactions = Column(Integer)
    parent_id = Column(Integer, ForeignKey('address.id'))

    def __init__(self, date, transactions, parent_id):
        self.date = date
        self.transactions = transactions
        self.parent_id = parent_id


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    address = Column(String(64), unique=True)
    eth_balance = Column(Float)
    token_balances = relationship(TokenBalance)
    daily_activities = relationship(DailyActivity)
    hourly_activities = relationship(HourlyActivity)
    counter_parties = relationship(Counterparties)

    def __init__(self, address, eth_balance, token_balances, daily_activities, hourly_activities, counter_parties):
        self.address = address
        self.eth_balance = eth_balance
        self.token_balances = token_balances
        self.daily_activities = daily_activities
        self.hourly_activities = hourly_activities
        self.counter_parties = counter_parties

