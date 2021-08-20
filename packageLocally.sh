#!/usr/bin/env bash

# sudo rm -fr dist build *egg*
echo y | pip uninstall nexus-python
pip install -r requirements.txt
pyb
WHL=$(find -type f -name "*.whl")
pip install ${WHL}  # --force-reinstall
