import dash_bootstrap_components as dbc

def get_navbar(pages):
    rows = [dbc.Col(dbc.NavLink(page['name'], href=page['relative_path'])) for page in pages]
    navbar = dbc.Navbar(
    dbc.Container([
        dbc.Row([dbc.Col("Logo")]),
        dbc.Row(rows)
    ]))
    return navbar
