from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

directors_ns = Namespace("directors")


@directors_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return DirectorSchema(many=True).dump(directors), 200


@directors_ns.route("/<int:uid>")
class DirectorView(Resource):
    def get(self, uid):
        director = director_service.get_one(uid)
        return DirectorSchema().dump(director), 200