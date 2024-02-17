import pandas as pd
import numpy as np
from sql import *

team_colors = {
    "Rouge": "danger",
    "Bleu": "primary",
    "Jaune": "warning",
    "Verte": "success",
    "GENERIC": "secondary",
}

# ------------ Functions --------------

def get_team_color(team_str):
    if team_str not in team_colors.keys():
        return team_colors["GENERIC"]

    return team_colors[team_str]


def get_all_team_colors():
    # Make SQL request 
    cols = ["color"]
    sql_cols = ", ".join(cols)
    req = f"select {sql_cols} from teams;"

    # Connect and request database
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    df_team_colors = db.select_to_df(req, cols)
    db.close()

    team_colors = df_team_colors.color.to_numpy()
    return team_colors


def get_all_teams():
    # Make SQL request 
    cols = ["team", "display_name"]
    sql_cols = ", ".join(cols)
    req = f"select {sql_cols} from users WHERE username <> 'admin';"

    # Connect and request database
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    df_teams = db.select_to_df(req, cols)
    db.close()

    # exctract name of all teams
    all_teams = list(df_teams.team.value_counts().index)

    return df_teams, all_teams
