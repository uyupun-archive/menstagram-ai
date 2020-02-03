import numpy as np
import keras.preprocessing.image as Image

from flask import jsonify
from keras.applications.vgg16 import preprocess_input
from api import app
from api import model

def predict():
    image_path = './trainer/learn_data/test/_ramen/663.jpg'
    image = Image.load_img(image_path, target_size = (224, 224))
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
    return jsonify([
        predict()
    ])