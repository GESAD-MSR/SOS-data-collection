
from flask import Flask
from flask_restful import Api, Resource


def create_app(config_name: str):
    app = Flask(__name__)
    api = Api(app)

    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}

    api.add_resource(HelloWorld, '/')
    return app
