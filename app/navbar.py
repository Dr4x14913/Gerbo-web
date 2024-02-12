import dash_bootstrap_components as dbc
from dash import html

def get_navbar(pages):
    logo = html.Img(src='assets/gerbouillette.jpg', height="100px"),

    rows = [dbc.Col(dbc.NavLink(page['name'], href=page['relative_path'])) for page in pages]
    navbar = dbc.Navbar(
    dbc.Container([
        # Place this logo to the left
        dbc.Row([dbc.Col(logo)]),
        dbc.Row(rows)
    ]))

    return navbar
