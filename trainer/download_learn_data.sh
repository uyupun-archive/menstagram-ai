#!/bin/bash

# ラーメンの画像(学習データ)の収集に必要なライブラリをインストールし, 画像を収集する

if [[ ! -e trainer/chromedriver ]]; then
  echo "'chromedriver is not exists.'"
  echo "Please download 'chromedriver' that matches your 'Google Chrome' version."
  echo "Download from http://chromedriver.chromium.org/downloads"
  echo "Then move 'chromedriver' file to 'trainer' directory."
else
  googleimagesdownload -ri -cd "trainer/chromedriver" -k "ラーメン" -f "jpg" -l 1000 -o trainer/downloads
  googleimagesdownload -ri -cd "trainer/chromedriver" -k "画像" -f "jpg" -l 1000 -o trainer/downloads
  googleimagesdownload -ri -cd "trainer/chromedriver" -k "写真" -f "jpg" -l 1000 -o trainer/downloads
  googleimagesdownload -ri -cd "trainer/chromedriver" -k "静止画" -f "jpg" -l 1000 -o trainer/downloads
fi