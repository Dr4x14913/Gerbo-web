import sys
sys.path.extend(["pages","."])
import dash
from sql import *
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
#-- Front functions
#--------------------------------------------------------------------------------------------------------

def get_navbar(pages, current_user)->html.Div:
    """TODO"""
    logged_txt = "Not logged" if current_user is None else current_user
    user = html.Div([logged_txt], id="user-display")
    rows = [
        (dbc.NavLink(page['name'], href=page['relative_path'], class_name='navlink'))
        for page in pages if not (page["name"] == "Home" or page['name'] == 'Backoffice' and current_user != 'admin') # home n'est pas pris en compte dans la navbar
    ] + [user]
    navbar = html.Div(children = rows, id='navbar')
    return navbar

#--------------------------------------------------------------------------------------------------------
#-- APP init
#--------------------------------------------------------------------------------------------------------
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

app.layout = html.Div(children=[
    # Header banner
    html.Div(children = [
        dcc.Link( # go back to home page when image is clicked
            html.Img(src='assets/logo.png', id='logo'),
            href="/home", refresh=False , id='logo-link-to-home'
        ),
        get_navbar(dash.page_registry.values(), None)
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
    Output(component_id='navbar', component_property='children'),
    Input(component_id='CURRENT_USER', component_property='data')
)
def navbar_callback(current_user):
    return get_navbar(dash.page_registry.values(), current_user)

#--------------------------------------------------------------------------------------------------------
#-- MAIN
#--------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")

