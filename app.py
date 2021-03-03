# -*- coding: utf-8 -*-
'''
FLASK APPLICATION
'''
# Import required packages
from flask import Flask
from flask_login import LoginManager
from flask_session import Session
import glob
import os

# Import configuration
from config import Config

# Initialize the database and import the user model for login
from application.models.shared import db
from application.models.user import User

# Initialize login manager and session
login_manager = LoginManager()
# sess = Session()


'''
FUNCTIONS
'''
def create_app():
    '''
    Create the application with the proper configuration
    '''
    app = Flask(
        __name__, 
        instance_relative_config=False,
        static_folder='application/static', 
        static_url_path='/static',
        template_folder='application/templates'
    )
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    # sess.init_app(app)

    # Add the login manager to all routes
    @login_manager.user_loader
    def load_user(user_id):
        '''
        Check for user and admin
        '''
        x = User.query.get(str(user_id))
        return x

    # Import and register the main routes
    with app.app_context():
        from application.routes import views as main_blueprint
        app.register_blueprint(main_blueprint)

        # Import and register the authentication routes
        from application.auth import authentication as auth_blueprint
        app.register_blueprint(auth_blueprint)

        # Create all database tables
        db.create_all()

    # Return the application
    return app


'''
RUN
'''
# Use the application factory to create the app
if __name__ == '__main__':
    app = create_app()

    # Run on debug to reload on change
    if hasattr(Config, 'ENVIRONMENT') and Config.ENVIRONMENT == 'development':
        app.run(port=5000, debug=True)
    
    # Run without debugging on production
    else:
        app.run(port=5000, debug=False)