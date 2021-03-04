# Joe Flask Template
#### APP STRUCTURE
```
- app.py
- config.py
- conda_environment.yml
- requirements.txt
- application
    - auth.py
    - routest.py
    - models
        - shared.py
        - user.py
    - testing
        - tests_base.py
        - user
            - tests.py
    - static
        - css
            - sytlesheet.css
        - images
    - templates
        - base.html
        - index.html
        - login.html
        - signup.html
```
#### ENVIRONMENT
`requirements.txt` contains the packages for pip installation. If using Anaconda to manage packages, create a new environment named `joe_flask_template` from `conda_environment.txt`.

#### TESTING
Execute the following command to run tests for the routes:
```
$ python -m unittest discover
```
This template includes a user test by default.