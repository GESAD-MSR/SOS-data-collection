# External modules
from flask import jsonify, request
from flask_restful import Resource

# Local modules
from ...models.entity.technology_entity import TechnologyEntity
from ...resources.repository.technology_repo import TechnologyRepo


class Technology(Resource):

    def __init__(self):
        super().__init__()
        self.repository = TechnologyRepo()

    def get(self):
        # doc = TechnologyData.objects().first()
        doc = self.repository.find_by_uid("5f42ff247a12fb6d8886b0fb")
        return jsonify(doc)

    def post(self):
        print('request here')
        request_body = request.get_json()
        print(type(request_body['tags']))

        new_tech = TechnologyEntity(
            name=request_body['name'],
            tags=request_body['tags']
        )

        self.repository.persist(new_tech)

        print(new_tech.to_dict())

        return jsonify(new_tech.to_dict())


class TechnologyList(Resource):

    def __init__(self):
        super().__init__()
        self.repository = TechnologyRepo()

    def get(self):
        # doc = TechnologyData.objects().first()
        docs = TechnologyData.objects()
        return jsonify(docs)
