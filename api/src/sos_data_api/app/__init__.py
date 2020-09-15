
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_mongoengine import MongoEngine
from .config.app_config import evn_config
from mongoengine import Document, StringField, IntField
from .web.resources.technology import Technology


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(evn_config[config_name])
    evn_config[config_name].init_app(app)

    api = Api(app)
    db = MongoEngine(app)

    api.add_resource(Technology, '/')

    return app
