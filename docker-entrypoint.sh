#!/usr/bin/env bash

. /venv/bin/activate
echo " -- Invoke pybuilder"
pyb

WHL=$(find -type f -name "*nexus*.whl")
pip install $WHL

cp -r src/main/scripts/static src/main/scripts/templates src/main/scripts/certificate.pem /venv/bin

python3 /venv/bin/nexus.py
