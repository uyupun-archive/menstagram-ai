import os
import logging
import numpy as np
import keras.preprocessing.image as Image

from flask import Flask, request, jsonify
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input

model = load_model('ml/judge-ramen-model.h5')
model._make_predict_function()

app = Flask(__name__)
app.config.from_pyfile('.env')
logging.basicConfig(filename = 'logs/flask.log', format = '[%(asctime)s] %(levelname)s: %(message)s', level = app.config['LOG_LEVEL'])

def predict():
    image_path = './ml/learn_data/test/_ramen/663.jpg'
    image = Image.load_img(image_path, target_size = (224, 224))
    x = Image.img_to_array(image)
    x = np.expand_dims(x, axis = 0)
    x = preprocess_input(x)
    ans = model.predict(x, 1)[0]
    other = ans[0]
    ramen = ans[1]
    return []

@app.route('/')
def index():
    return 'Menstagram AI'

@app.route('/api/v1/ramen/judge', methods = ['POST'])
def judge_ramen():
    # file = request.files.get('image1')
    # file.save(os.path.join(file.filename))

    res = predict()

    return jsonify([
        res
    ])

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True, threaded = False)