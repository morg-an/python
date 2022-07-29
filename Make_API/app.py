from crypt import methods
from lib2to3.pgen2.token import NEWLINE
from urllib import request
import numpy as np
import pandas as pd
import csv
from flask import Flask, render_template
from flask import request
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
cors = CORS(app)

# necessary for /update to work
@ app.route('/')
def index():
    return render_template('new.html')

# gets csv list and returns as JSON
@ app.route('/get')
def home():
    csv_list = pd.read_csv('todo.csv')
    result = csv_list.to_json(orient="index")
    return dumped

# gets csv list and converts it into a dictionary
@app.route('/new')
def new():
    csv_list = pd.read_csv('todo.csv')
    result = csv_list.to_json(orient="index")
    parsed = json.loads(result)
    return parsed

# Gets form input for new task as dictionary
# Writes CSV file with a header line of column names
# Iterates through all to-dos and writes each row to CSV
@app.route('/update', methods=['GET', 'POST'])
def update():
    output = request.get_data()
    result = json.loads(output)
    csv_columns = ['todo', 'start_date', 'due_date']
    with open('todo.csv', 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for todo in result:
            writer.writerow(result[todo])
     return result

# Notes to self:
# Select virtual environment    View > Command Palette > Python: Select Interpreter
# Run app                       "python3 -m flask run" in the terminal
