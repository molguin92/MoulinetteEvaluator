from flask import make_response, request
from flask_restful import Resource

from moulinette import app, docker_client

class EvaluatorResource(Resource):
    def post(self):
        return make_response(docker_client.containers.run("hello-world"))

    def get(self):
        return self.post()
