from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Labels(Resource):
    def get(self, address):
        pass


class EthBalance(Resource):
    def get(self, address):
        pass


class TokenBalances(Resource):
    def get(self, address):
        pass


class DailyActivities(Resource):
    def get(self, address):
        pass


class DayActivities(Resource):
    def get(self, address, days):
        pass


class HourActivities(Resource):
    def get(self, address, hours):
        pass


class InEth(Resource):
    def get(self, address):
        pass


class OutEth(Resource):
    def get(self, address):
        pass


class TopLabels(Resource):
    def get(self, num_of_rows, offset):
        pass


class TokenExchangeSupplyRatio(Resource):
    def get(self, token):
        pass


class TokenTxsNum(Resource):
    def get(self, token):
        pass


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
api.add_resource(Labels, "/address/<string:address>/eth_balance", endpoint='eth_balance')
api.add_resource(Labels, "/address/<string:address>/token_balances", endpoint='token_balances')
api.add_resource(Labels, "/address/{address}/daily_activities/{date_range}", endpoint='daily_activities')
api.add_resource(Labels, "/address/{address}/day_activities/{days}", endpoint='day_activities')
api.add_resource(Labels, "/address/{address}/hour_activities/{hours}", endpoint='hour_activities')
api.add_resource(Labels, "/address/{address}/in_eth", endpoint='in_eth')
api.add_resource(Labels, "/address/{address}/out_eth", endpoint='out_eth')
api.add_resource(Labels, "/top_labels/{num_of_rows}/{offset}", endpoint='top_labels')
api.add_resource(Labels, "/token/{token}/exchange_supply_ratio", endpoint='exchange_supply_ratio')
api.add_resource(Labels, "/token/{token}/txs_num", endpoint='txs_num')
api.add_resource(Labels, "/token/{token}/volume_on_exchanges", endpoint='volume_on_exchanges')
api.add_resource(Labels, "/token/{token}/top_exchanges", endpoint='top_exchanges')
api.add_resource(Labels, "/token/{token}/notable_wallets", endpoint='notable_wallets')
api.add_resource(Labels, "/token/{token}/top_transactions", endpoint='top_transactions')
api.add_resource(Labels, "/token/{token}/top_balances", endpoint='top_balances')
api.add_resource(Labels, "/token/{token}/seniority_distribution", endpoint='seniority_distribution')
api.add_resource(Labels, "/token/{token}/num_unique_addresses", endpoint='num_unique_addresses')


if __name__ == "__main__":
    app.run(debug=True)
