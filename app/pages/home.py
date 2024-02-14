import dash
from dash import html, dcc, callback, Input, Output, State, callback_context
from login_manager import login, logout#, get_current_user
import dash_bootstrap_components as dbc

#------------------------------------------------------------------------------------
#-- Layout
#------------------------------------------------------------------------------------
dash.register_page(__name__)

login_form = dbc.Form(
    [
        dbc.Label("Username", html_for="username"),
        dbc.Col(
            dbc.Input(type="text", id="username", placeholder="Enter your username"),
            width=4,
        ),
        dbc.Label("Password", html_for="password"),
        dbc.Col(
            dbc.Input(type="password", id="password", placeholder="Enter your password"),
            width=4,
        ),
        dbc.Button("Submit", color="primary", type="submit", id="submit"),
    ],
    id='login-form',
)

logout_btn = dbc.Button("Logout", color="danger", id="logout-btn", className = "d-none")

layout = html.Div([
    login_form,
    logout_btn,
], id="main-frame")

#------------------------------------------------------------------------------------
#-- Callbacks
#------------------------------------------------------------------------------------
@callback(
    [Output("user-display", "children"), Output('CURRENT_USER', 'data')],
    [Input("submit", "n_clicks"), Input("logout-btn", "n_clicks")],
    [State("password", "value"), State("username", "value"), State('CURRENT_USER', 'data')]
)
def login_and_logout_callback(login_clicks, logout_clicks, p, u, cu):
    ctx = callback_context

    if not ctx.triggered:
        # No active trigger means this is the first render, so show current user status
        return (f"Logged as: {cu}", cu)

    button_id = ctx.triggered_id  # Gets the id of the triggered component

    if button_id == "submit":
        res = login(u, p)
        return (f"Logged as: {res}", res) if res != 0 else (f"Logged as: {cu}", cu)
    elif button_id == "logout-btn":
        res = logout()
        return (f"Logged as: {res}", res)

    # return f"Logged as: {get_current_user()}"


#------------------------------------------------------------------------------------
@callback(
    [Output("login-form", "className"), Output("logout-btn", "className")],
    [Input("main-frame", "children"), Input("user-display", "children")],   # Triggering element is the number of times this component has been clicked, not the input values
    [State('CURRENT_USER', 'data')]
)
def display_form_callback(main, username, cu):
    if cu == "None":
        return ("", "d-none")
    else:
        return ("d-none", "")

