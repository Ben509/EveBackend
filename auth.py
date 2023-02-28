from flask import Blueprint, request
from db import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)
users = db.users
@auth.route('/login')
def login():
    return "Login"


@auth.route('/signup')
def signup():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = users.find({}, {"email": email})
    if user:
        return "Account already exists"
    new_user = {"email": email, "name": name, "password": generate_password_hash(password, method='sha256')}
    users.insert_one(new_user)

@auth.route('/logout')
def logout():
    return 'Logout'