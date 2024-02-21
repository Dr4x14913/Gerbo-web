import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from teams_manager import get_team_color, get_all_teams

dash.register_page(__name__)


# ------------- Page Components -------------------

layout = html.Div([
    html.Div(id="game-display")
])

# ------------ Callback functions ---------------

