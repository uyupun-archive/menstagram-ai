import numpy as np
import keras.preprocessing.image as Image

from flask import request, jsonify
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from api import app

@app.before_first_request
def init():
    global model
    model = load_model('trainer/judge-ramen-model.h5')
    model._make_predict_function()

def predict(image):
    image = Image.load_img(image, target_size = (224, 224))
    x = Image.img_to_array(image)
    x = np.expand_dims(x, axis = 0)
    x = preprocess_input(x)
    ans = model.predict(x, 1)[0]
    other = ans[0]
    ramen = ans[1]
    res = True if ramen > other else False
    return res

@app.route('/api/v1/ramen/judge', methods = ['POST'])
def judge_ramen():
    images = []
    if 'image1' in request.files:
        images.append(request.files.get('image1'))
    if 'image2' in request.files:
        images.append(request.files.get('image2'))
    if 'image3' in request.files:
        images.append(request.files.get('image3'))
    if 'image4' in request.files:
        images.append(request.files.get('image4'))

    res = []
    for image in images:
        res.append(predict(image))

    return jsonify(res)