import dash_bootstrap_components as dbc
from dash import html
from login_manager import get_current_user

def get_navbar(pages)->html.Div:
    """TODO"""
    user = html.Div([f"Log as {get_current_user()}"], id="user-display")
    rows = [(dbc.NavLink(page['name'], href=page['relative_path'], class_name='navlink')) for page in pages] + [user]
    navbar = html.Div(children = rows, id='navbar')
    return navbar
