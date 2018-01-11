from flask import make_response, request
from flask_restful import Resource
from moulinette import job_serializer, redis_queue
from moulinette.evaluator.logic import test_program


class EvaluatorResource(Resource):
    def post(self):
        job = redis_queue.enqueue(test_program, "hello")
        return job_serializer.dumps(job.id)

class JobResource(Resource):
    def get(self, id):
        job = redis_queue.fetch_job(job_serializer.loads(id))
        return job.result


