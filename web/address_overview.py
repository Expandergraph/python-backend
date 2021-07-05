import sys

sys.path.append("..")
from data_model.address_overview import *
from data_model.base import session
from flask_restful import Resource
from flask import jsonify


class Labels(Resource):
    def get(self, address):
        labels = session.query(Label).filter_by(address=address).all()
        return jsonify(list(map(lambda x: x.name, labels)))


class EthBalance(Resource):
    def get(self, address):
        balance = session.query(TokenBalance).filter_by(address=address, token='ETH').first()
        return jsonify(balance=balance.balance)


class TokenBalances(Resource):
    def get(self, address):
        balances = session.query(TokenBalance).filter(TokenBalance.address == address, TokenBalance.token != 'ETH').all()
        return jsonify(list(map(lambda x: {'token': x.token, 'address': x.address}, balances)))


class DailyActivities(Resource):
    def get(self, address):
        daily_activities = session.query(DailyActivity).filter_by(address=address).all()
        return jsonify(list(map(lambda x: {'date': x.date.strftime("%y%m%d"), 'transactions': x.transactions},
                                daily_activities)))


class DayActivities(Resource):
    def get(self, address, days):
        pass


class HourActivities(Resource):
    def get(self, address, hours):
        pass