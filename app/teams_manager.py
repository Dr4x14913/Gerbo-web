import pandas as pd
import numpy as np
from sql import *

# ------------ Functions --------------
def get_team_color(team_str):
    # Make SQL request
    cols = ["color"]
    sql_cols = ", ".join(cols)
    req = f"select {sql_cols} from teams where name = '{team_str}';"

    # Connect and request database
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    color = db.select(req)
    db.close()

    return color


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
