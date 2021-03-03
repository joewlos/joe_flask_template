# -*- coding: utf-8 -*-
'''
USER WITH ID, EMAIL, PASSWORD, AND NAME
'''
# Import required packages
from application.models.shared import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    '''
    Simple user
    '''
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # Hash the password when setting
    def set_password(self, secret):
        self.password = generate_password_hash(secret)

    # Check the validity of the password
    def check_password(self, secret):
        return check_password_hash(self.password, secret)
    
    # Add the user to the database
    def create_new_user(self):
        db.session.add(self)
        db.session.commit()
        return None