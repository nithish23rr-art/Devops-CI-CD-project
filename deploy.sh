#!/bin/bash
./venv/bin/pip install Flask
./venv/bin/pip install -r requirements.txt
nohup python3 web_application.py > app.log 2>&1 &
