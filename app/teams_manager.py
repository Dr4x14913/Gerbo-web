import pandas as pd
from sql import *

db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)

team_colors = {
    "Rouge": "danger",
    "Bleu": "primary",
    "Jaune": "warning",
    "GENERIC": "secondary",
}

def get_team_color(team_str):
    if team_str not in team_colors.keys():
        return team_colors["GENERIC"]

    return team_colors[team_str]


# ------------ Initialize team variables -----------
def get_all_teams():
    cols = ["team", "display_name"]
    sql_cols = ", ".join(cols)

    req = f"select {sql_cols} from users WHERE username <> 'admin';"
    df_teams = db.select_to_df(req, cols)

    all_teams = list(df_teams.team.value_counts().index)
    return df_teams, all_teams

