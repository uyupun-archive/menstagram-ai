import os
import numpy as np
import keras.preprocessing.image as Image

from keras.models import load_model
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.preprocessing.image import ImageDataGenerator

model = load_model('judge-ramen-model.h5')

test_data_paths = [
    './learn_data/test/_ramen/',
    './learn_data/test/_sutaba/',
    './learn_data/test/_other/',
]

for test_data_path in test_data_paths:
    images = os.listdir(test_data_path)
    for image in images:
        image_path = test_data_path + image
        image = Image.load_img(image_path, target_size = (224, 224))
        x = Image.img_to_array(image)
        x = np.expand_dims(x, axis = 0)
        x = preprocess_input(x)
        res = model.predict(x, 1)[0]
        for i, score in enumerate(res):
            if i == 0:
                print('{}: {:.2%} '.format('_other', score), end = '')
            elif i == 1:
                print('{}: {:.2%} '.format('_ramen', score), end = '')
            else:
                print('{}: {:.2%} '.format('_sutaba', score))