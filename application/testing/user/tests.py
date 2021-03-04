# -*- coding: utf-8 -*-
'''
TEST THE USER MODEL
'''
# Import required packages
from flask import url_for
from application.testing.tests_base import BaseTestCase
from application.models.user import User


'''
LOGIN
'''
class UserViewsTests(BaseTestCase):
    def test_users_can_login(self):
        response = self.client.post(
            url_for('authentication.login'),
            data={
                'email': 'test@test.com', 
                'password': 'test'
            }
        )
        self.assert_redirects(response, url_for('views.index'))