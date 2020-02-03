import logging

from flask import Flask

app = Flask(__name__)
app.config.from_object('api.config')
logging.basicConfig(filename = 'api/logs/flask.log', format = '[%(asctime)s] %(levelname)s: %(message)s', level = app.config['LOG_LEVEL'])

from api.controllers import index_controller, judge_ramen_controller