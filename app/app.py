import sys
sys.path.extend(["pages","."])
import dash
from sql import *
from navbar import get_navbar
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

#--------------------------------------------------------------------------------------------------------
#-- SQL init
#--------------------------------------------------------------------------------------------------------

#Establish the connection to MariaDB
db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
print("Connection successful!")


# Create the "teams" table
db.insert("""
CREATE TABLE IF NOT EXISTS `teams` (
    `id` INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30) UNIQUE,
    `color` VARCHAR(30),
    `registration_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )""")

# db.insert(f"""
#     INSERT INTO teams (name)
#     SELECT * FROM (SELECT '{default_team}' as name) AS tmp
#     WHERE NOT EXISTS (
#         SELECT name FROM teams WHERE name = '{default_team}'
#     ) LIMIT 1
# """)
# print(f'{default_team} team created!')


# Create the "users" table
db.insert("""
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(30) NOT NULL UNIQUE,
    `password` VARCHAR(100) NOT NULL,
    `display_name` VARCHAR(50),
    `team` VARCHAR(50),
    `avatar_name` VARCHAR(50),
    `registration_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT `existing_team`
        FOREIGN KEY (team) REFERENCES teams (name)
    )""")
# Insert an admin user with username "admin", password set at "123" and email "admin@example.com"
db.insert(f"""
    INSERT INTO users (username, password)
    SELECT * FROM (SELECT 'admin' as username, '123' as password) AS tmp
    WHERE NOT EXISTS (
        SELECT username FROM users WHERE username = 'admin'
    ) LIMIT 1
""")
print('Admin user created!')



#--------------------------------------------------------------------------------------------------------
#-- APP init
#--------------------------------------------------------------------------------------------------------

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[

    # Header banner
    html.Div(children = [
        dcc.Link( # go back to home page when image is clicked
            html.Img(src='assets/logo (2).png', id='logo'), 
            href="/home", refresh=False , id='logo-link-to-home'
        ), 
        get_navbar(dash.page_registry.values())
    ], id='header'),

    # Page
    dash.page_container,

    # Properties storage
    # current user
    dcc.Store(id='CURRENT_USER', storage_type='session', data=None),
    # url location
    dcc.Location(id='url')

], id='app-container')


#--------------------------------------------------------------------------------------------------------
#-- CALLBACKS
#--------------------------------------------------------------------------------------------------------

# Redirects user to home page on first app load ('/' -> '/home')
@app.callback(
    Output(component_id='url', component_property='pathname'),
    Input(component_id='url', component_property='pathname')
)
def redirect_to_home(current_pathname):
    if current_pathname != '/':
        raise PreventUpdate
    else:
        return '/home'

# Redirects user to home page on first app load ('/' -> '/home')
@app.callback(
    Output(component_id='user-display', component_property='children'),
    Input(component_id='CURRENT_USER', component_property='data')
)
def show_current_user(current_user):
    if current_user is None:
        return 'Not logged'
    else:
        return f'Logged as {current_user}'

#--------------------------------------------------------------------------------------------------------
#-- MAIN
#--------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
