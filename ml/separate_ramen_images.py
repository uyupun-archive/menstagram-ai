# downloads以下にある画像をtrain/validation/testに分類する

import os
import shutil

def get_category_name(src_path):
    if 'ラーメン' in src_path:
        return '_ramen'
    elif 'スタバ' in src_path:
        return '_sutaba'
    return '_other'

def make_dirs(dist_path, category_name):
    os.makedirs(dist_path + 'train/' + category_name, exist_ok = True)
    os.makedirs(dist_path + 'validation/' + category_name, exist_ok = True)
    os.makedirs(dist_path + 'test/' + category_name, exist_ok = True)

def get_borders(images_len):
    train_border = int(images_len * 0.8)
    validation_border = int(images_len * 0.9)
    test_border = images_len
    return train_border, validation_border, test_border

def main():
    src_paths = [
        './downloads/ラーメン/',
        './downloads/スタバ/',
        './downloads/画像/',
        './downloads/写真/',
        './downloads/静止画/',
    ]
    dist_path = './learn_data/'

    for src_path in src_paths:
        images = os.listdir(src_path)
        category_name = get_category_name(src_path)
        make_dirs(dist_path, category_name)
        train_border, validation_border, test_border = get_borders(len(images))

        for i, image in enumerate(images):
            file_name = str(i + 1) + '.jpg'
            if i < train_border:
                shutil.copy(src_path + image, dist_path + 'train/' + category_name + '/' + file_name)
            elif i < validation_border:
                shutil.copy(src_path + image, dist_path + 'validation/' + category_name + '/' + file_name)
            elif i < test_border:
                shutil.copy(src_path + image, dist_path + 'test/' + category_name + '/' + file_name)

if __name__ == '__main__':
    main()