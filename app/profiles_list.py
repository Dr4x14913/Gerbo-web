#! /usr/bin/python3
from sql import *
import pandas as pd

AVATAR_DIR = "assets/avatars/"

profiles = {
    "maria": {
        "État": "déstructurée",
        "Localisation": "le plan d'eau"
    },
    "fufu": {
        "État": "Nu",
        "État des fesses": "Va chercher du pq putain"
    },
    "glenn": {
        "État du curé": "Venère dorènavant le fessier du Saint Glenn"
    },
    "francis": {
        "État de la pinte": "Pleine comme une pute",
        "Type de boisson": "Vomi",
        "Kink connu": "Regurgitation en levrette",
        "Kink connu 2": "Le Caca"
    },
    "mimole": {
        "Localisation": "Inconnue... Mais avez vous cherché derrière l'Église ??"
    },
    "sn": {
        "Localistaion":"Gravier",
        "État":"Gravier",
        "Levier de vitesse":"Gravier"
    },
    "captain":{
        "État":"Héhéhé"
    },
    "didjo":{
        "Localisation": "Rue St-Michel",
        "État de la main": "Brisée",
        "État de la vitre": "Intacte"
    }
}

def get_profile(user):
    # Make SQL request
    cols = ["display_name", "team"]
    sql_cols = ", ".join(cols)
    req = f"select {sql_cols} from users WHERE username = '{user}';"

    # Connect and request database
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    df_infos = db.select_to_df(req, cols)
    db.close()

    # get user informations
    res = {}
    if df_infos.shape[0] != 0:
        res["Nom"] = df_infos.display_name.iloc[0]
        res["Équipe"] = df_infos.team.iloc[0]

    # get profil calenbours
    calenbours = {}
    if user in profiles.keys():
        calenbours = profiles[user]

    # merge informations and calenbours
    res.update(calenbours)
    return res

def get_avatar(user):
    # Make SQL request
    cols = ["avatar_name"]
    sql_cols = ", ".join(cols)
    req = f"select {sql_cols} from users WHERE username = '{user}';"

    # Connect and request database
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    df_avatar = db.select_to_df(req, cols)
    db.close()

    # if no avatar image
    if df_avatar.shape[0] == 0 or df_avatar.avatar_name.iloc[0] is None:
        # return default avatar
        return "assets/logo.png"

    # make avatar path
    avatar_path = AVATAR_DIR + df_avatar.avatar_name.iloc[0]
    return avatar_path

def set_display_name(user, name):
    req = f"UPDATE users SET display_name='{name}' WHERE username = '{user}'"
    try:
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        db.insert(req)
        db.close()
    except Exception as e:
        return 1
    return 0

def get_display_name(user):
    # Make SQL request
    cols = ["display_name"]
    sql_cols = ", ".join(cols)
    req = f"select {sql_cols} from users WHERE username = '{user}';"

    # Connect and request database
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    df = db.select_to_df(req, cols)
    db.close()

    # if no display_name
    if df.shape[0] == 0:
        # return the user name
        return user

    display_name = df.display_name.iloc[0]
    return display_name

def set_password(user, pswd):
    req = f"UPDATE users SET password='{pswd}' WHERE username = '{user}'"
    try:
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        db.insert(req)
        db.close()
    except Exception as e:
        return 1
    return 0
