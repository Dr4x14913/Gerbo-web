import dash
from dash import html, dcc, callback, Input, Output, State, callback_context
from login_manager import login, logout#, get_current_user
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

#------------------------------------------------------------------------------------
#-- Layout
#------------------------------------------------------------------------------------
dash.register_page(__name__)   

login_form = dbc.Form(
    [
        html.Div(id='username-entry',
                children = [dbc.Label("Username"), dbc.Input(type="text", id="username", placeholder="Enter your username")]),
        html.Div(id='password-entry',
                children=[dbc.Label("Password"),dbc.Input(type="password", id="password", placeholder="Enter your password")]),
        dbc.Button(children="Submit", color="primary", type="submit", id="submit", n_clicks=None),
        dbc.Label(id="login-error", style={'display': 'None'}, children = "Error: username or password is incorrect")
    ],
    id='login-form',
)

logout_btn = dbc.Button("Logout", color="danger", id="logout-btn", className="d-none")

layout = html.Div([
    login_form,
    logout_btn,
], id="main-frame")

#------------------------------------------------------------------------------------
#-- Callbacks
#------------------------------------------------------------------------------------
@callback(
    [Output("user-display", "children"), Output('CURRENT_USER', 'data'), Output("login-error", "style")],
    [Input("submit", "n_clicks"), Input("logout-btn", "n_clicks")],
    [State("password", "value"), State("username", "value"), State('CURRENT_USER', 'data')],
    prevent_initial_call=True
)
def login_and_logout_callback(login_clicks, logout_clicks, pswd_in, user_in, current_user):

    if login_clicks is None:
        raise PreventUpdate

    ctx = callback_context

    if not ctx.triggered:
        # No active trigger means this is the first render, so show current user status
        return (f"Logged as: {current_user}", current_user, None)

    button_id = ctx.triggered_id  # Gets the id of the triggered component

    if button_id == "submit" and user_in is not None and pswd_in is not None:
        res = login(user_in, pswd_in)
        if res != 0:
            return (f"Logged as: {res}", res, None)
        else:
            return (f"Logged as: {current_user}", current_user, {'color': 'danger'})
    elif button_id == "logout-btn":
        res = logout()
        return (f"Logged as: {res}", res, None)
    else:
        return (f"Logged as: {current_user}", current_user, None)

#------------------------------------------------------------------------------------
@callback(
    [Output("login-form", "className"), Output("logout-btn", "className")],
    [Input("user-display", "children")],
    [State('CURRENT_USER', 'data')],
    prevent_initial_call=True
)
def display_form_callback(username, current_user):
    if current_user == "None":
        return ("", "d-none")
    else:
        return ("d-none", "")


