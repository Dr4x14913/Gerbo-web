#! /usr/bin/python3
from sql import *

# def get_current_user():
#     return CURRENT_USER

def logout():
    return "None"

def login(user, password):
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    # If user contain any of this chararters then return 1: " ", ";"
    if check_user(user):
        return 0
    db_pass = db.select(f"Select password from users where username='{user}'")
    if len(db_pass) == 0:
        return -1
    if  db_pass[0][0] == password:
        return user
    else:
        return 0

# Create the storage component for holding the current user data


# @app.callback(
#     dash.dependencies.Output('CURRENT_USER', 'data'),
#     [dash.dependencies.Input('login-button', 'n_clicks')],
#     [dash.dependencies.State('username-input', 'value'),
#      dash.dependencies.State('password-input', 'value')]
# )
# def login(n_clicks, user, password):
#     if n_clicks is None:
#         return ''  # Return an empty string when nothing has been clicked yet
#     db = Sql(MYSQL_DATABASE, DB_HOST=db, DB_USER=MYSQL MYSQL_PASSWORD)
#     # If user contain any of this characters then return 1: " ", ";"
#     if check_user(user):
#         return ''
#     db_pass = db.select(f"Select password from users where username={user}")
#     if len(db_pass) == 0:
#         return ''
#     if db_pass[0][0] == password:
#         return user  # Return the username on successful login
#     else:
#         return ''

# @app.callback(
#     dash.dependencies.Output('logout-button', 'n_clicks'),
#     [dash.dependencies.Input('CURRENT_USER', 'data')]
# )
# def logout(current_user):
#     if current_user is None:
#         return 0  # Return zero to ensure no clicks are registered when there's no user logged in
#     return 1  # Register a click for the logout button


def check_user(user):
    if any(char in user for char in " ;"):
        return 1
    else:
        return 0
