# -*- coding: utf-8 -*-
'''
TEST THE APPLICATION
'''
# Import required packages
from flask_testing import TestCase
from config import Testing
from app import create_app


'''
BASE
'''
class BaseTestCase(TestCase):
    '''
    Base case for testing
    '''
    def create_app(self):
        app = create_app()

        # Adjust the configuration for testing
        app.config.from_object('config.Testing')
        
        # Return the application for testing
        return app