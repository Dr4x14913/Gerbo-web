from sql import *

def get_days():
    req = "SELECT day FROM schedule GROUP BY day " + order_by_day()
    db  = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    res = db.select(req)
    db.close()
    return [i[0] for i in res]

def get_activities(day):
    req = f"SELECT hour, activity FROM schedule WHERE day='{day}'ORDER BY hour"
    db  = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    res = db.select(req)
    db.close()
    return res


def get_menus(day):
    req = f"SELECT time, menu, orga FROM menus WHERE day='{day}' " + order_by_period()
    db  = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    res = db.select(req)
    db.close()
    return res

def order_by_day():
    """ Sql syntax to order by day of week spell in french"""
    jours      = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    order_case = ' '.join([f"WHEN day = '{j}' THEN {jours.index(j)}" for j in jours])
    return "ORDER BY CASE " + order_case + " END ASC"

def order_by_period():
    """ Sql syntax to order by day periods in french"""
    jours      = ['Matin', 'Midi', 'Soirée', 'Soir',]
    order_case = ' '.join([f"WHEN time = '{j}' THEN {jours.index(j)}" for j in jours])
    return "ORDER BY CASE " + order_case + " END ASC"
