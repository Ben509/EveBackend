from flask import Blueprint, request
from db import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)
users = db.users
@auth.route('/login')
def login():
    return "Login"

@auth.route('/signup', methods=['POST'])
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

@auth.route('/logout')
def logout():
    return 'Logout'