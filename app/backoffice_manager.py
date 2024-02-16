#! /usr/bin/python3
from sql import *
import pandas as pd


def get_db_data_as_df():
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    df = db.select_to_df("Select username, display_name, team, avatar_name from users where username != 'admin'", ("username", "display_name", "team", "avatar_name"))
    db.close()
    return df

def update_table(update_dict):
    """update_dict should be contruct as follow: {username: {col1: val1, col2: val2 ...}, username2: {...}}"""
    try:
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        for user in update_dict:
            sql_req = "UPDATE users SET " + ", ".join([f"{c}='{v}'" for c,v in update_dict[user].items()]) + f" WHERE username='{user}'"
            db.insert(sql_req)
        db.close()
    except Exception as e:
        return f"Error: {e}"
    return ""
