import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from teams_manager import all_teams, df_teams, get_team_color

dash.register_page(__name__)

team_components = {}

for team in all_teams:
    # récupération des données
    df_inte = df_teams[df_teams.team == team].copy()
    users = df_inte.display_name.to_numpy()

    # conception tableaux html des équipes
    header = [html.Thead(html.Tr([html.Th(team)]))]
    body = [html.Tbody([
            html.Tr([html.Td(user)]) for user in users
        ])]
    color = get_team_color(team)
    
    # sauvegarde des tableaux
    team_components[team] = dbc.Table(header + body, id=f"team_table-{team}", color=color, bordered=True)

# ------------- Page Components -------------------
layout = html.Div(
    [table_component for team, table_component in team_components.items()]
)