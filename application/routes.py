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
    send_from_directory,
    session
)
from flask import current_app as app
from flask_login import current_user
import random

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
    # Get the time
    now = datetime.now().strftime("%m/%d/%Y, %-I:%M%p")

    # Get the username
    if current_user.is_authenticated:
        username = current_user.name
    else:
        username = None
    
    # Get the session data
    data = {
        'i': session.get('i'),
        'ip': session.get('ip'),
        'browser': session.get('browser'),
        'time': session.get('time')
    }

    # Render the template
    return render_template(
        'index.html',
        time=now,
        username=username,
        data=data
    )

@views.route('/example_image')
def example_image():
    '''
    Return an example image from the static folder
    '''
    return send_from_directory(app.static_folder, 'images/panda.jpg')

@views.route('/example_session')
def example_session():
    '''
    Add a random value to the session, with timestamp and additional info
    '''
    i = random.randint(0, 10)
    timestamp = datetime.now().strftime("%m/%d/%Y, %-I:%M%p")
    session['i'] = i
    session['time'] = timestamp
    session['ip'] = request.environ['REMOTE_ADDR']
    session['browser'] = request.user_agent.browser
    return '{0} at {1}'.format(i, timestamp)