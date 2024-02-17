#! /usr/bin/python3
from sql import *
import pandas as pd


def get_db_data_as_df(table, cols, cond="1"):
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    df = db.select_to_df("Select " + ", ".join(cols) + " from " + table + " where " + cond, cols)
    db.close()
    return df

def update_table(table, update_dict, colname):
    """
    colname is the name of the column that is use in the condition
    update_dict should be contruct as follow: {cond1: {colname_value1: val1, col2: val2 ...}, colname_value2: {...}}
    """
    try:
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        for user in update_dict:
            sql_req = f"UPDATE {table} SET " + ", ".join([f"{c}='{v}'" for c,v in update_dict[user].items()]) + f" WHERE {colname}='{user}'"
            db.insert(sql_req)
        db.close()
    except Exception as e:
        return f"Error: {e}"
    return ""
