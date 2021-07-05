import sys

sys.path.append("..")
from data_model.token_exchanges_overview import *
from data_model.base import session
from flask_restful import Resource
from flask import jsonify


class TokenExchangeSupplyRatioResource(Resource):
    def get(self, token):
        ratio = session.query(TokenExchangeSupplyRatio).filter_by(token=token).first()
        return jsonify({"ratio": ratio.ratio})


class TokenBalancesComp(Resource):
    def get(self, token):
        balances_comp = session.query(TokenBalancesComparison).filter_by(token=token).all()
        return jsonify(list(map(lambda x: {'date': x.date.strftime("%y%m%d"),
                                           'dex traders': x.pct_of_dex_traders,
                                           'exchanges': x.pct_of_exchanges}, balances_comp)))
