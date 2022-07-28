import numpy as np
import pandas as pd
from flask import Flask
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
cors = CORS(app)

csv_list = pd.read_csv('todo.csv')

# @ app.route('/')
# def home():
#     return csv_list.to_json(orient="index")

# Returns contents of CSV as JSON


@ app.route('/get')
def home():
    result = csv_list.to_json(orient="index")
    # returns dict object
    parsed = json.loads(result)
    dumped = json.dumps(parsed, indent=4)
    return dumped

# Returns contents of CSV as Python Dict.


@app.route('/new')
def new():
    result = csv_list.to_json(orient="index")
    parsed = json.loads(result)
    return parsed


# Notes to self:
# Assign path to URL            @app.route("/")
# Select virtual environment    View > Command Palette > Python: Select Interpreter
# Run app                       "python3 -m flask run" in the terminal

