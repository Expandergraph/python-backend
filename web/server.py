import sys
sys.path.append("..")
from flask import Flask
from flask_restful import Api, Resource

from address_overview import *
from wallet_profiler import *
from top_labels import *
from token_exchanges_overview import *

app = Flask(__name__)
api = Api(app)


class TokenVolumeOnExchanges(Resource):
    def get(self, token):
        pass


class TopExchanges(Resource):
    def get(self, token):
        pass


class NotableWallets(Resource):
    def get(self, token):
        pass


class TopTransactions(Resource):
    def get(self, token):
        pass


class TopBalance(Resource):
    def get(self, token):
        pass


class SeniorityDistribution(Resource):
    def get(self, token):
        pass


class NumUniqueAddresses(Resource):
    def get(self, token):
        pass


api.add_resource(Labels, "/address/<string:address>/labels", endpoint='labels')
api.add_resource(EthBalance, "/address/<string:address>/eth_balance", endpoint='eth_balance')
api.add_resource(TokenBalances, "/address/<string:address>/token_balances", endpoint='token_balances')
api.add_resource(DailyActivities, "/address/<string:address>/daily_activities", endpoint='daily_activities')
api.add_resource(DayActivities, "/address/{address}/day_activities/{days}", endpoint='day_activities')
api.add_resource(HourActivities, "/address/{address}/hour_activities/{hours}", endpoint='hour_activities')
api.add_resource(InEth, "/address/<string:address>/in_eth", endpoint='in_eth')
api.add_resource(OutEth, "/address/<string:address>/out_eth", endpoint='out_eth')
api.add_resource(TopLabels, "/top_labels", endpoint='top_labels')
api.add_resource(TokenExchangeSupplyRatioResource, "/token/<string:token>/exchange_supply_ratio", endpoint='exchange_supply_ratio')
api.add_resource(TokenBalancesComp, "/token/<string:token>/balance_comp", endpoint='balance_comp')
api.add_resource(TokenVolumeOnExchanges, "/token/<string:token>/volume_on_exchanges", endpoint='volume_on_exchanges')
api.add_resource(TopExchanges, "/token/<string:token>/top_exchanges", endpoint='top_exchanges')
api.add_resource(NotableWallets, "/token/<string:token>/notable_wallets", endpoint='notable_wallets')
api.add_resource(TopTransactions, "/token/<string:token>/top_transactions", endpoint='top_transactions')
api.add_resource(TopBalance, "/token/<string:token>/top_balances", endpoint='top_balances')
api.add_resource(SeniorityDistribution, "/token/<string:token>/seniority_distribution", endpoint='seniority_distribution')
api.add_resource(NumUniqueAddresses, "/token/<string:token>/num_unique_addresses", endpoint='num_unique_addresses')


if __name__ == "__main__":
    app.run(debug=True)
