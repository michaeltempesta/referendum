# app/__init__.py
from flask import Flask
from flask_restful import Api
from .resources.PollResource import PollResource

app = Flask(__name__)
api = Api(app)

api.add_resource(PollResource, '/poll', '/poll/<int:poll_id>')
