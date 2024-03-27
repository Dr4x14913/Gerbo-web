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
        for cond in update_dict:
            sql_req = f"UPDATE {table} SET " + ", ".join([f'{c}="{v}"' for c,v in update_dict[cond].items()]) + f' WHERE {colname}="{cond}"'
            db.insert(sql_req)
        db.close()
    except Exception as e:
        return f"Error: {e}"
    return ""

def insert_row(table, cols, values):
    try:
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        sql_req = f"INSERT INTO {table} (" + ", ".join(cols) + ") VALUES (" + ", ".join([f'"{i}"' for i in values])  + ")"
        db.insert(sql_req)
        db.close()
    except Exception as e:
        return f"Error: {e}"
    return ""

def del_row(table, row, col):
    try:
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        sql_req = f'DELETE FROM {table} WHERE {col}="{row}"'
        db.insert(sql_req)
        db.close()
    except Exception as e:
        return f"Error: {e}"
    return ""

def get_disabled_pages():
    try:
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        sql_req = f'SELECT * FROM disabled_pages'
        pages = [p[0].lower() for p in db.select(sql_req)]
        db.close()
    except Exception as e:
        pages = []
    return pages;

def log(a):
    print(a, flush=True)
