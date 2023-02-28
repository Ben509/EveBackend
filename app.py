from flask import Flask, request, url_for, redirect
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.eve
entries = db.entries

@app.route('/',  methods = ['POST'])
def index():
    if request.method == 'POST':
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        symptoms = json.loads(request.form['symptoms'])
        entries.insert_one({'start_date': start_date, 'end_date': end_date, 'symptoms': symptoms})
        return "Done"