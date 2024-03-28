from sql import *
import pandas as pd


def get_days():
    req = "SELECT day FROM schedule GROUP BY day " + order_by_day()
    db  = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    res = db.select(req)
    db.close()
    print(res, flush=True)
    return [i[0] for i in req[0]]

def get_schedule():
    cols = ['day','hour', 'activity']
    req  = f"SELECT {', '.join(cols)} FROM schedule {order_by_day()}, hour";
    db   = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    df   = db.select_to_df(req, cols).to_dict('split')
    db.close()
    print(df, flush=True)
    return df

def order_by_day():
    """ Sql syntax to order by day of week spell in french"""
    jours      = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    order_case = ' '.join([f"WHEN day = '{j}' THEN {jours.index(j)}" for j in jours])
    return "ORDER BY CASE " + order_case + " END ASC"
