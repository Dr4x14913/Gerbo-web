from sql import *
import pandas as pd

def get_all_puzzles(cols):
    req  = f'select {", ".join(cols)} from puzzles LEFT JOIN puzzles_hints on puzzles.name=puzzles_hints.puzzle ORDER BY {cols[0]}'
    # print(req, flush=True)
    db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    df_puzz = db.select_to_df(req, cols).to_dict('list')
    db.close()
    # print(df_puzz, flush=True)
    return df_puzz

def get_solutions(puzzle):
    req    = f'select solution from puzzles where name = "{puzzle}"'
    db     = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    soluce = db.select(req)[0][0]
    db.close()
    return soluce.split('|') # multiples solutions can be accepted

def get_team(user):
    db       = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    req      = f'SELECT team from users WHERE username="{user}" LIMIT 1'
    team_res = db.select(req)
    db.close()
    return team_res[0][0]

def success_team_of_user(user, puzzle):
    try:
        team = get_team(user)
        if team is None or team == 'None':
            return 1, "Your are not in a valid team"

        req = f'INSERT INTO puzzles_success (puzzle, team) VALUES ("{puzzle}", "{team}")'
        db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
        db.insert(req)
        db.close()
        return 0, f'Team {team} has completed the {puzzle}'
    except Exception as e:
        return 1, f"{e}"

def has_succeeded(team, puzzle):
    req   = f'select count(*) from puzzles_success where team="{team}" and puzzle="{puzzle}"'
    db    = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
    count = int(db.select(req)[0][0])
    db.close()
    if count > 0:
        return 1
    else:
        return 0
