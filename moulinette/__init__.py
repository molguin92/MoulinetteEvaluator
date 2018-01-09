import logging
from logging.handlers import RotatingFileHandler

from flask_restful import Api
from moulinette.LoggingFlask import LoggingFlask
import docker
from redis import Redis
from rq import Queue

API_PREFIX = '/api/v1'

app = LoggingFlask(__name__)
app.logger.addHandler(RotatingFileHandler('.moulinette.log',
                                          maxBytes=5242880,  # 5 MiB
                                          backupCount=3))
app.logger.setLevel(logging.INFO)

api = Api(app)
docker_client = docker.from_env()
redis_queue = Queue(connection=Redis())

import moulinette.views
