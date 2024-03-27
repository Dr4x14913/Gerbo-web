import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from teams_manager import get_team_color, get_all_teams
from backoffice_manager import get_disabled_pages

dash.register_page(__name__)


# ------------- Page Components -------------------

layout = html.Div([
    html.Div(id="teams-display")
])

# ------------ Callback functions ---------------

@callback(Output("teams-display", "children"), Input("teams-display", "children"))
def make_team_table(nothing):

    if str(__name__).split('.')[-1] in get_disabled_pages():
        return html.Div(['You are not allowed to be here, please go away before Didjo la canaille te botte le derch'])
    # données des équipes
    df_teams, all_teams = get_all_teams()

    # Tableaux par équipes
    team_components = []
    for team in all_teams:
        # données de l'équipe
        df_inte = df_teams[df_teams.team == team].copy()
        users = df_inte.display_name.to_numpy()

        # tableau html
        color = get_team_color(team)
        header = [html.Thead(html.Tr([html.Th(team)]))]
        body = [html.Tbody([html.Tr([html.Td(user)]) for user in users])]

        table = dbc.Table(header + body, id=f"team_table-{team}", color=color, bordered=True)
        team_components.append(table)

    return team_components

