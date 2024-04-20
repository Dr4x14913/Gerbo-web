#! /usr/bin/python3
from sql import * # W: Wildcard import sql
import pandas as pd

def get_pronos():
    db          = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    res = db.select(f"Select name from pronos")
    db.close()
    return [i[0] for i in res]

def get_choices(name):
    db          = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    choices_str = db.select(f"Select choices from pronos WHERE name='{name}'")
    db.close()
    return choices_str[0][0].split(",")

def get_label(name):
    db    = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    label = db.select(f"Select label from pronos WHERE name='{name}'")
    db.close()
    return label[0][0]

def set_prono_res(prono, user, res):
    try:
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        db.insert(f"INSERT INTO pronosResults (prono_name, username, vote) VALUES ('{prono}', '{user}', '{res}')")
        db.close()
    except Exception as e: # W: Catching too general exception Exception
        return f"Error: {e}"
    return ""

def get_last_vote(prono, user):
    try:
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        last_vote = db.select(f"SELECT vote FROM pronosResults WHERE username='{user}' AND prono_name = '{prono}' ORDER BY time DESC LIMIT 1")
        db.close()
    except Exception as e: # W: Catching too general exception Exception
        return f"Error: {e}"
    if len(last_vote) == 0:
        return "None"
    return last_vote[0][0]

def get_prono_count(prono):
    votes = {}
    try:
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        users_that_voted = db.select(f"SELECT username from pronosResults where prono_name='{prono}' group by username")
        for user in users_that_voted:
            vote = get_last_vote(prono, user[0])
            if vote not in votes:
                votes[vote] = 1
            else:
                votes[vote] += 1
        db.close()
    except Exception as e: # W: Catching too general exception Exception
        return f"Error: {e}"
    return votes
