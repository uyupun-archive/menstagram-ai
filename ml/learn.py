# VGG16 + 転移学習で学習する

import numpy as np
import keras.preprocessing.image as Image

from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input, decode_predictions

model = VGG16(weights = 'imagenet', include_top = True)

image_path = './learn_data/test/675.jpg'
image = Image.load_img(image_path, target_size = (224, 224))
x = Image.img_to_array(image)
x = np.expand_dims(x, axis = 0)
x = preprocess_input(x)

res = model.predict(x)
res = decode_predictions(res, top = 3)[0]
print(res[0][1])

for _, name, score in res:
    print('{}: {:.2%}'.format(name, score))