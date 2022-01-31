# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run

from flask import Flask, g, render_template, request
from numpy import number

import pandas as pd
import sqlite3

from app import db_app  # import login_log,login_ip


# We create the web app, and run it with flask run.
# (set "FLASK_ENV" variable to "development" first!!!)

app = Flask(__name__)


# Create main page (fancy)
@app.route('/')

def main():
     return render_template("main.html")


@app.route('/view/', methods=['POST', 'GET'])
def view():
    if request.method == 'GET':
        return render_template('view.html')
    else:
        try:
            n = int(request.form['number'])
            g.result = db_app.random_messages(n)
            return render_template('view.html',number = request.form['number'])
        except:
            return render_template('view.html',number="error")

# File uploads and interfacing with complex Python
# basic version


# nontrivial version: makes a prediction and shows a viz
@app.route('/submit/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            db_app.insert_message(request)
            return render_template('submit.html', user=request.form['user'], message=request.form['message'])
        except:
            return render_template('submit.html', user='error', message='error')


if __name__ == '__main__':
    app.run()