from moulinette import api, API_PREFIX
from moulinette.evaluator.views import EvaluatorResource, JobResource

api.add_resource(EvaluatorResource,
                 API_PREFIX + '/evaluator',
                 API_PREFIX + '/evaluator')

api.add_resource(JobResource,
                 API_PREFIX + '/evaluator/<string:id>',
                 API_PREFIX + '/evaluator/<string:id>')
