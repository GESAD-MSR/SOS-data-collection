from flask import jsonify
from flask_restful import Resource
from ...resources.repository.technology_repo import TechnologyRepo


class Technology(Resource):

    def __init__(self):
        super().__init__()
        self.repository = TechnologyRepo()

    def get(self):
        # doc = TechnologyData.objects().first()
        doc = self.repository.find_by_uid("5f42ff247a12fb6d8886b0fb")
        return jsonify(doc)


class TechnologyList(Resource):

    def __init__(self):
        super().__init__()
        self.repository = TechnologyRepo()

    def get(self):
        # doc = TechnologyData.objects().first()
        docs = TechnologyData.objects()
        return jsonify(docs)
