#! /usr/bin/python3
from sql import *

# def get_current_user():
#     return CURRENT_USER

def logout():
    return "None"

def login(user, password):
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    # If user contain any of this chararters then return 1: " ", ";"
    if user is None:
        return 0
    if any(char in user for char in " ;"):
        return 0
    db_pass = db.select(f"Select password from users where username='{user}'")
    if len(db_pass) == 0:
        return 0
    if  db_pass[0][0] == password:
        return user
    else:
        return 0
