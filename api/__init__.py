import logging

from flask import Flask
from keras.models import load_model

app = Flask(__name__)
app.config.from_object('api.config')

logging.basicConfig(filename = 'api/logs/flask.log', format = '[%(asctime)s] %(levelname)s: %(message)s', level = app.config['LOG_LEVEL'])

# model = load_model('../trainer/judge-ramen-model.h5')
# model._make_predict_function()

from api.controllers import index_controller, judge_ramen_controller