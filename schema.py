from graphene import ObjectType, String, Boolean, ID, Field, Int, List
from dotenv import load_dotenv
import os
import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.customers_api import CustomersApi
import json
from collections import namedtuple

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

class Address(ObjectType):
  address_line_1 = String()
  address_line_2 = String()
  address_line_3 = String()
  locality = String()
  sublocality = String()
  sublocality_2 = String()
  sublocality_3 = String()
  administrative_district_level_1 = String()
  administrative_district_level_2 = String()
  administrative_district_level_3 = String()
  postal_code = String()
  country = String()
  first_name = String()
  last_name = String()
  organization = String()

class Card(ObjectType):
  id =	String()
  card_brand =	String()
  last_4 =	String()
  exp_month =	Int()
  exp_year =	Int()
  cardholder_name =	String()
  billing_address =	Field(Address)
  fingerprint =	String()

class CustomerPreferences(ObjectType):
  email_unsubscribed =	Boolean()

class CustomerGroupInfo(ObjectType):
  id = String()
  name = String()

class Customer(ObjectType):
  id = String()
  created_at = String()
  updated_at = String()
  cards = List(Card)
  given_name = String()
  family_name = String()
  nickname = String()
  company_name = String()
  email_address = String()
  address = Field(Address)
  phone_number = String()
  birthday = String()
  reference_id = String()
  note = String()
  preferences = Field(CustomerPreferences)
  groups = List(CustomerGroupInfo)
  creation_source = String()


class Query(ObjectType):
  customers = List(Customer)

  def resolve_customers(self, info):
    customers_api = CustomersApi()
    customers_api.api_client.configuration.access_token = ACCESS_TOKEN
    customers = customers_api.list_customers()
    return customers.customers
