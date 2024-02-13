import dash
from dash import html, dcc, callback, Input, Output, State
from login_manager import log, get_current_user
import dash_bootstrap_components as dbc

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

layout = html.Div([
    login_form,
])

# Define callback for updating 'out' div content when 'submit' button is clicked
@callback(
    Output("user-display", "children"),
    [Input("submit", "n_clicks")],   # Triggering element is the number of times this component has been clicked, not the input values
    [State("password", "value"), State("username", "value")]  # Include states so that they are passed as inputs to callback function
)
def display_username_callbask(n_clicks, p, u):
    if n_clicks is not None:  # If 'submit' hasn't been clicked yet
        log(u,p)
    return f"Logged as: {get_current_user()}"
