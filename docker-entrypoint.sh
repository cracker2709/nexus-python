#!/usr/bin/env bash

. /tmp/docker-env/bin/activate

echo " -- Install requirements"
pip install --upgrade pip
pip install -r requirements.txt

echo " -- Invoke pybuilder"
pyb
