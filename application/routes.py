# -*- coding: utf-8 -*-
'''
APPLICATION ROUTES BLUEPRINT
'''
# Import required packages
from datetime import datetime
from flask import (
    Blueprint, 
    render_template, 
    request,
    send_from_directory
)
from flask import current_app as app
from flask_login import current_user

# Create the blueprint
views = Blueprint(
    'views', 
    __name__
)


'''
EXAMPLE ROUTES
'''
@views.route('/')
def index():
    '''
    Return an example template with the time
    '''
    now = datetime.now()
    if current_user.is_authenticated:
        username = current_user.name
    else:
        username = None
    return render_template(
        'index.html',
        time=now.strftime("%m/%d/%Y, %-I:%M%p"),
        username=username
    )

@views.route('/example_image')
def example_image():
    '''
    Return an example image from the static folder
    '''
    return send_from_directory(app.static_folder, 'images/panda.jpg')