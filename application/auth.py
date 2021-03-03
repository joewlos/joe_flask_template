# -*- coding: utf-8 -*-
'''
AUTHENTICATION ROUTES BLUEPRINT
'''
# Import required packages
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for
)
from flask import current_app as app
from flask_login import (
    login_user,
    logout_user,
    login_required
)
from application.models.user import User

# Create the blueprint
authentication = Blueprint(
    'authentication', 
    __name__
)


'''
AUTHENTICATION ROUTES
'''
@authentication.route('/login', methods=['GET', 'POST'])
def login():
    '''
    Display the login form on GET and login on POST
    '''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        # Check if the user exists and if the password is correct
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            flash('Please check your login details and try again.')
            return render_template('login.html')
        else:
            login_user(user, remember=remember)
            return redirect(url_for('views.index'))

    # Render the template for GET
    else:
        return render_template('login.html')

@authentication.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    Display the sign up form on GET and sign up on POST
    '''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        # Check that all fields are not null
        if not email or not password or not name:
            flash('Please fill in all fields.')
            return render_template('signup.html')

        # Check if the user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists.')
            return render_template('signup.html')

        # Create the user
        new_user = User(
            email=email, 
            name=name
        )
        new_user.set_password(password)
        new_user.create_new_user()

        # Visit the login page
        return redirect(url_for('authentication.login'))

    # Render the sign up page
    else:
        return render_template('signup.html')

@authentication.route('/logout')
@login_required
def logout():
    '''
    Logout a user
    '''
    logout_user()
    return redirect(url_for('views.index'))
    return 'Logout'