from moulinette import api, API_PREFIX
from moulinette.evaluator.views import EvaluatorResource

api.add_resource(EvaluatorResource, API_PREFIX + '/evaluator',
                 API_PREFIX + '/evaluator')
