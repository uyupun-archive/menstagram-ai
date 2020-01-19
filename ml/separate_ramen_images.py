# downloads以下にある画像をtrain/validation/testに分類する

import os
import shutil

src_path = './downloads/ラーメン/'
dist_path = './learn_data/'

images = os.listdir(src_path)

os.makedirs(dist_path + 'train', exist_ok = True)
os.makedirs(dist_path + 'validation', exist_ok = True)
os.makedirs(dist_path + 'test', exist_ok = True)

images_len = len(images)
train_border = int(images_len * 0.8)
validation_border = int(images_len * 0.9)
test_border = images_len

for i, image in enumerate(images):
    file_name = str(i + 1) + '.jpg'
    if i < train_border:
        shutil.copy(src_path + image, dist_path + 'train/' + file_name)
    elif i < validation_border:
        shutil.copy(src_path + image, dist_path + 'validation/' + file_name)
    elif i < test_border:
        shutil.copy(src_path + image, dist_path + 'test/' + file_name)