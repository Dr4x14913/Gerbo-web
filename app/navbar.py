import dash_bootstrap_components as dbc
from dash import html

def get_navbar(pages)->html.Div:
    """TODO"""
    user = html.Div([f"Not logged"], id="user-display")
    rows = [(dbc.NavLink(page['name'], href=page['relative_path'], class_name='navlink')) for page in pages] + [user]
    navbar = html.Div(children = rows, id='navbar')
    return navbar
