# downloads以下にある画像をtrain/validation/testに分類する

import os
import shutil

def get_class_name(src_path):
    if 'ラーメン' in src_path:
        return 'ramen'
    return 'other'

def make_dirs(dist_path, class_name):
    os.makedirs(dist_path + 'train/' + class_name, exist_ok = True)
    os.makedirs(dist_path + 'validation/' + class_name, exist_ok = True)
    os.makedirs(dist_path + 'test/' + class_name, exist_ok = True)

def get_borders(images_len):
    train_border = int(images_len * 0.8)
    validation_border = int(images_len * 0.9)
    test_border = images_len
    return train_border, validation_border, test_border

def main():
    src_paths = [
        'trainer/downloads/ラーメン/',
        'trainer/downloads/画像/',
        'trainer/downloads/写真/',
        'trainer/downloads/静止画/',
    ]
    dist_path = 'trainer/learn_data/'

    for src_path in src_paths:
        images = os.listdir(src_path)
        class_name = get_class_name(src_path)
        make_dirs(dist_path, class_name)
        train_border, validation_border, test_border = get_borders(len(images))

        for i, image in enumerate(images):
            file_name = str(i + 1) + '.jpg'
            if i < train_border:
                shutil.copy(src_path + image, dist_path + 'train/' + class_name + '/' + file_name)
            elif i < validation_border:
                shutil.copy(src_path + image, dist_path + 'validation/' + class_name + '/' + file_name)
            elif i < test_border:
                shutil.copy(src_path + image, dist_path + 'test/' + class_name + '/' + file_name)

if __name__ == '__main__':
    main()