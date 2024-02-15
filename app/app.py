import sys
sys.path.extend(["pages","."])
import dash
from sql import *
from navbar import get_navbar
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

#--------------------------------------------------------------------------------------------------------
#-- SQL init
#--------------------------------------------------------------------------------------------------------
#Establish the connection to MariaDB
db = Sql(MYSQL_DATABASE, DB_HOST='db', DB_USER=MYSQL_USER, DB_PASS=MYSQL_PASSWORD)
print("Connection successful!")

# Create the "users" table
db.insert("""
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(30) NOT NULL UNIQUE,
    `password` VARCHAR(100) NOT NULL,
    `display_name` VARCHAR(50),
    `team` VARCHAR(50),
    `avatar_name` VARCHAR(50),
    `registration_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )""")
# Insert an admin user with username "admin", password set at "123" and email "admin@example.com"
db.insert("""
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
current_user_storage = dcc.Store(id='CURRENT_USER', storage_type='session', data="None")
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Div([ # Div holding location
        dcc.Location(id='url'),], id='location'),
    # Main div
    html.Div(children = [html.Img(src='assets/logo.png', id='logo'),
                        get_navbar(dash.page_registry.values())], id='header'),
    dash.page_container, current_user_storage,
], id='app-container')
@app.callback(
    Output('location', 'children'),
    [Input('url', 'pathname')]
)
def redirect_to_home(pathname):
    if pathname == '/':
        return dcc.Location(id='redirect-to-home', pathname='/home')
#--------------------------------------------------------------------------------------------------------
#-- MAIN
#--------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
