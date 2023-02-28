from bson import json_util
from flask import Flask, request
from pymongo import MongoClient
import json
from auth import auth as auth_blueprint
from main import main as main_blueprint
from db import entries
from db import db
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

client = MongoClient('172.22.58.1', 27017)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
# app.register_blueprint(auth_blueprint)
# app.register_blueprint(main_blueprint)
users = db.users

@app.route('/signup/', methods = ['POST'])
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        user = users.find_one({"email": email})
        if user:
            return "Account already exists"
        new_user = {"email": email, "name": name, "password": generate_password_hash(password, method='sha256')}
        users.insert_one(new_user)
        return "Done"

@app.route('/get-entries/', methods = ['GET'])
def get():
    if request.method == "GET":
        return json_util.dumps(entries.find({}))

@app.route('/create-entry',  methods = ['POST'])
def set_entry():
    if request.method == 'POST':
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        symptoms = json.loads(request.form['symptoms'])
        entries.insert_one({'start_date': start_date, 'end_date': end_date, 'symptoms': symptoms})
        return "Done"

if __name__== '__main__':
    app.run()