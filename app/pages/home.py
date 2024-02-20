import dash
from login_manager import login
from dash import html, dcc, callback, Input, Output, State, callback_context
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

#------------------------------------------------------------------------------------
#-- Layout
#------------------------------------------------------------------------------------
dash.register_page(__name__)

# Define phantom children (components that will be used in callbacks but aren't displayed yet)
phantom_style = {'display': 'none'}
phantom_children = [dbc.Button(id="logout-btn", n_clicks=None, style=phantom_style),
                    dbc.Button(id="login-btn", n_clicks=None, style=phantom_style),
                    html.Div(id='login-error', style=phantom_style),
                    dbc.Input(id="username", style=phantom_style),
                    dbc.Input(id="password", style=phantom_style)
                    ]
# Define layout
layout = html.Div(id='login-logout', children=phantom_children)

#------------------------------------------------------------------------------------
#-- Callbacks
#------------------------------------------------------------------------------------

# Displays either:
# - login form if user is not logged yet
# - logout form if user is already logged
@callback(
    Output(component_id='login-logout', component_property='children'),
    Input(component_id='CURRENT_USER', component_property='data'),
    State(component_id='login-error', component_property='style')
)
def display_login_or_logout(current_user, login_error_style):
    if current_user is None:
        return login_form(login_error_style=login_error_style)
    else:
        return logout_form(current_user=current_user)

# Logs the user out when logout button is clicked
@callback(
    Output(component_id='CURRENT_USER', component_property='data', allow_duplicate=True),
    Input(component_id='logout-btn', component_property='n_clicks'),
    prevent_initial_call=True
)
def logout(n_clicks:int):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return None

# Tries to log the user in when login button is clicked
@callback(
    [Output(component_id='login-error', component_property='style'),
    Output("CURRENT_USER", component_property='data', allow_duplicate=True)],
    Input(component_id='login-btn', component_property='n_clicks'),
    [State(component_id="password", component_property="value"), State(component_id="username", component_property="value")],
    prevent_initial_call=True
)
def try_login(n_clicks:int, password, username):
    if n_clicks is None:
        raise PreventUpdate
    else:
        successful_login = login(username, password)
        if successful_login==0:
            # Show error
            return {}, None
        else:
            return phantom_style, successful_login


#------------------------------------------------------------------------------------
#-- Front functions
#------------------------------------------------------------------------------------

def logout_form(current_user:str):
    """TODO:doc"""
    logout_info = html.Div(children=f"Vous êtes connectés en tant que {current_user}.", id='logout-infos')
    logout_btn = dbc.Button("Logout", color="danger", id="logout-btn", n_clicks=None)
    loggin_error = html.Div(id='login-error', style=phantom_style)
    return html.Div(id='logout-form', children=[logout_info, logout_btn, loggin_error])


def login_form(login_error_style):
    """TODO: doc"""

    # Define username entry
    username_text = html.Div(children='Username')
    username_input = dbc.Input(type="text", id="username", placeholder="Enter your username")
    username_entry = [username_text, username_input]

    # Define password entry
    password_text = html.Div(children='Password')
    password_input = dbc.Input(type="password", id="password", placeholder="Enter your password")
    password_entry = [password_text, password_input]

    # Define login button
    login_btn = [dbc.Button(children="Submit", color="primary", id="login-btn", n_clicks=None)]

    # Define login error div
    login_error = [html.Div(id='login-error', style=login_error_style, children = "Error: username or password is incorrect")]

    return dbc.Form(username_entry+password_entry+login_btn+login_error, id='login-form')


