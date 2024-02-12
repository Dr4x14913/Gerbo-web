#! /usr/bin/python3
from sql import *
CURRENT_USER = None

def get_current_user():
    return CURRENT_USER

def check_user(user):
    if any(char in user for char in " ;"):
        return 1
    else:
        return 0

def log(user, password):
    global CURRENT_USER
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    # If user contain any of this chararters then return 1: " ", ";"
    if check_user(user):
        return 1
    db_pass = db.select(f"Select password from users where username='{user}'")
    if len(db_pass) == 0:
        return -1
    if  db_pass[0][0] == password:
        CURRENT_USER = user
        return 0
    else:
        return 1


