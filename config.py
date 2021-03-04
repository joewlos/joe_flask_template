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
DEVELOPMENT AND PRODUCTION
'''
class Config:
    '''
    Set Flask configuration for import in app.py
    '''
    # Check if we are on the dev environment
    ENVIRONMENT = environ.get('ENVIRONMENT')

    # General configuration
    SECRET_KEY = environ.get('SECRET_KEY')

    # Redis
    SESSION_TYPE = environ.get('SESSION_TYPE')
    SESSION_REDIS = redis.from_url(environ.get('SESSION_REDIS'))
    PERMANENT_SESSION_LIFETIME = 30  # Seconds

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


'''
TESTING
'''
class Testing(Config):
    '''
    Adjust configuration for testing
    '''
    TESTING = True
    WTF_CSRF_ENABLED = False
