from flask import Flask, jsonify, request
from flask_graphql import GraphQLView
from graphene import Schema
from schema import Query
from dotenv import load_dotenv

app = Flask(__name__)

view_func = GraphQLView.as_view(
    'graphql', schema=Schema(query=Query, auto_camelcase=False), graphiql=True)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=view_func)

if __name__ == '__main__':
    app.run(debug=True)