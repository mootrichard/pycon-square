import squareconnect
from flask import Flask, jsonify, request
from json import dumps, loads
from flask_restful import Resource, Api, reqparse
from squareconnect.rest import ApiException
from squareconnect.apis.locations_api import LocationsApi
from squareconnect.apis.transactions_api import TransactionsApi
import uuid
from dotenv import load_dotenv
import os

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

parser = reqparse.RequestParser()

app = Flask(__name__)
api = Api(app)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

class Payments(Resource):
    def get(self):
        transactions_api = TransactionsApi()
        locations_api = LocationsApi()
        transactions_api.api_client.configuration.access_token = ACCESS_TOKEN
        locations_api.api_client.configuration.access_token = ACCESS_TOKEN
        locations_response = locations_api.list_locations()
        transactions_response = transactions_api.list_transactions(locations_response.locations[0].id)
        return list(map(lambda x: x.to_dict(), transactions_response.transactions))
    def post(self):
        request_data = request.get_json(force=True)
        transactions_api = TransactionsApi()
        locations_api = LocationsApi()
        transactions_api.api_client.configuration.access_token = ACCESS_TOKEN
        locations_api.api_client.configuration.access_token = ACCESS_TOKEN
        locations_response = locations_api.list_locations()
        transactions_response = transactions_api.charge(locations_response.locations[0].id, {
            'idempotency_key': str(uuid.uuid4().hex),
            'card_nonce': request_data['card_nonce'],
            'amount_money': {
                'amount': 100,
                'currency': 'USD'
            }
        })
        return transactions_response.to_dict(), 200

class Locations(Resource):
    def get(self):
        api_instance = LocationsApi()
        api_instance.api_client.configuration.access_token = ACCESS_TOKEN
        api_response = api_instance.list_locations()
        return list(map(lambda x: x.to_dict(), api_response.locations))

api.add_resource(Payments, '/pay')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    app.run(debug=True)