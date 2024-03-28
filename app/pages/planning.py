import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State
from dash.exceptions import PreventUpdate
from backoffice_manager import get_disabled_pages
from planning_manager import get_schedule, get_days
#------------------------------------------------------------------------------------
dash.register_page(__name__)

phantom_style    = {'display': 'none'}
phantom_children = [
]


layout = html.Div([
    html.Div(phantom_children, id='planning-content')
])


#------------------------------------------------------------------------------------
@callback(
    Output("planning-content", "children"),
    [Input("planning-content", "children")],
    [State("CURRENT_USER", "data")]
)
def display_profile_callback(dummy, user):
    if str(__name__).split('.')[-1] in get_disabled_pages():
        return html.Div(['You are not allowed to be here, please go away before Didjo la canaille te botte le derch'])

    # schedule = get_schedule()
    for day in get_days():
        for activity, time in get_activities(day):

    return html.Div([])
#------------------------------------------------------------------------------------
