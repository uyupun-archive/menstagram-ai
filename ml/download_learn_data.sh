#!/bin/bash

# ラーメンの画像(学習データ)の収集に必要なライブラリをインストールし, 画像を収集する

if !(type "python" > /dev/null 2>&1);then
  echo "'Python' is not exists."
  echo "Please install 'Python'."
elif !(type "pip" > /dev/null 2>&1);then
  echo "'pip' is not exists."
  echo "Please install 'pip'."
elif !(type "googleimagesdownload" > /dev/null 2>&1);then
  echo "'google_images_download' is not Exists."
  echo "Please execute 'pip install google_images_download'."
elif [ ! -e 'chromedriver' ];then
  echo "'chromedriver is not exists.'"
  echo "Please download 'chromedriver' that matches your 'Google Chrome' version."
  echo "Download from http://chromedriver.chromium.org/downloads"
  echo "Then move 'chromedriver' file to 'ml' directory."
else
  googleimagesdownload -ri -cd "./chromedriver" -k "ラーメン" -f "jpg" -l 1000
  googleimagesdownload -ri -cd "./chromedriver" -k "画像" -f "jpg" -l 1000
  googleimagesdownload -ri -cd "./chromedriver" -k "写真" -f "jpg" -l 1000
  googleimagesdownload -ri -cd "./chromedriver" -k "静止画" -f "jpg" -l 1000
fi