#!/bin/bash
set -e

echo "creating dest folder..."
rm -rf dest && mkdir dest

echo "copying source code..."
cp -r index.py some_file.txt requirements.txt dest

echo "install production dependencies..."
cd dest
pip install -r requirements.txt -t .

echo "zip code..."
zip -r index.zip *

echo "cleanup..."
ls | grep -v index.zip | xargs rm -rf
