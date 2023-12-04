#!/bin/bash

python -m venv .venv

pip install -r requirements.txt
python -m build leap_packages/leapc-cffi
pip install leap_packages/leapc-cffi/dist/leapc_cffi-0.0.1.tar.gz
pip install -e leap_packages/leapc-python-api

source .venv/Scripts/activate
