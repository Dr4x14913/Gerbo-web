import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd


content =  dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Show db", tab_id="tab-1"),
                    dbc.Tab(label="Modify db", tab_id="tab-2"),
                ],
                id="card-tabs",
                active_tab="tab-1",
            )
        ),
        dbc.CardBody(html.P(id="card-content", className="card-text")),
    ]
)


#------------------------------------------------------------------------------------
dash.register_page(__name__)

layout = html.Div([
    html.Div([], id='backoffice-content'),
    html.Br(),
])

#------------------------------------------------------------------------------------
@callback(
    Output("backoffice-content", "children"),
    [Input("backoffice-content", "children")],
    [State("CURRENT_USER", "data")]
)
def access(dummy, user):
    if user == "admin":
        return content
    else:
        return dbc.Alert('Permission denied', color="danger")
