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
