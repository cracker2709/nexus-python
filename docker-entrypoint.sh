#!/usr/bin/env bash

. /venv/bin/activate
echo " -- Invoke pybuilder"
pyb

WHL=$(find -type f -name "*nexus*.whl")
pip install $WHL

python3 /venv/bin/nexus.py
