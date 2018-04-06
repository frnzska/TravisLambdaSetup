#!/bin/bash
set -e

echo "creating dest folder..."
rm -rf dest && mkdir dest

echo "copying source code..."
cp -r `ls -A | grep -v "dest\|tests"` dest

echo "install production dependencies..."
cd dest
pip install -r requirements.txt -t .

echo "zip code..."
zip -r index.zip *

echo "cleanup..."
ls | grep -v index.zip | xargs rm -rf
