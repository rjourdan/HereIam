#!/bin/bash

export PKG_DIR="python/lib/python3.7/site-packages"

rm -f python.zip

rm -rf ${PKG_DIR} && mkdir -p ${PKG_DIR}

cp *.py ${PKG_DIR}

docker run -v "$(pwd):/foo" -w /foo --rm lambci/lambda:build-python3.7 \
    pip install -r requirements.txt -t ${PKG_DIR}

zip -r python.zip ${PKG_DIR}