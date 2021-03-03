# -*- coding: utf-8 -*-
'''
CONFIGURATION FOR FLASK
'''
# Import packages
from dotenv import load_dotenv
from os import environ
import redis

# Load local environment variables for development
load_dotenv()


'''
CLASSES
'''
class Config:
    '''
    Set Flask configuration for import in app.py
    '''
    # Check if we are on the dev environment
    ENVIRONMENT = environ.get('ENVIRONMENT')

    # General configuration
    SECRET_KEY = environ.get('SECRET_KEY')

    # Flask session
    # SESSION_TYPE = environ.get('SESSION_TYPE')
    # SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS'))

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False