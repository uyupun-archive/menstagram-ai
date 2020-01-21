import os
import numpy as np
import keras.preprocessing.image as Image

from keras.models import load_model
from keras.applications.vgg16 import preprocess_input

model = load_model('judge-ramen-model.h5')

test_data_paths = [
    './learn_data/test/_ramen/',
    './learn_data/test/_other/',
]

for i, test_data_path in enumerate(test_data_paths):
    if i == 0:
        print('ramen')
    else:
        print('other')

    images = os.listdir(test_data_path)
    for image in images:
        image_path = test_data_path + image
        image = Image.load_img(image_path, target_size = (224, 224))
        x = Image.img_to_array(image)
        x = np.expand_dims(x, axis = 0)
        x = preprocess_input(x)
        ans = model.predict(x, 1)[0]
        for j, score in enumerate(ans):
            if j == 0:
                print('{}: {:.2%} '.format('other', score), end = '')
            else:
                print('{}: {:.2%} '.format('ramen', score))