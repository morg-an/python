import numpy as np
import pandas as pd
from flask import Flask
import json
app = Flask(__name__)

csv_list = pd.read_csv('todo.csv')

# @ app.route('/')
# def home():
#     return csv_list.to_json(orient="index")


@ app.route('/')
def home():
    result = csv_list.to_json(orient="index")
    parsed = json.loads(result)
    dumped = json.dumps(parsed, indent=4)
    return dumped


@app.route('/new')
def new():
    return "<h1>Add New To Do</h1>"


# Notes to self:
# Assign path to URL            @app.route("/")
# Select virtual environment    View > Command Palette > Python: Select Interpreter
# Run app                       "python3 -m flask run" in the terminal
# Open in browser               ctrl + click the url in the terminal
# Ensure only safe char in url  import re; match_object = re.match("[a-zA-Z]+", name)

# Helpful Resources:
# https://code.visualstudio.com/docs/python/tutorial-flask#:~:text=To%20run%20the%20app%20outside,using%20python%20%2Dm%20flask%20run%20.
# https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
# https://flask-restful.readthedocs.io/en/latest/
