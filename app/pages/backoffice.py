import dash
from dash.exceptions import PreventUpdate
from dash import html, dcc, callback, Input, Output, State, ALL
import dash_bootstrap_components as dbc
import pandas as pd
from backoffice_manager import get_db_data_as_df, update_table

#------------------------------------------------------------------------------------
dash.register_page(__name__)

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
layout = html.Div([
    html.Div([content], id='backoffice-content'),
    html.Br(),
    html.Div([], id="sql-error", className="danger"),
])

#------------------------------------------------------------------------------------
#-- Callbacks
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

@callback(
    Output("card-content", "children"),
    [Input("card-tabs", "active_tab")],
)
def tab_content_callback(tab):
    if tab == "tab-1":
        table = dbc.Table.from_dataframe(get_db_data_as_df(), striped=True, bordered=True, hover=True)
        content = table
    else:
        # Display a dash_bootstrap_components table where each field is an input text
        data         = get_db_data_as_df().to_dict('split')
        username_idx = data['columns'].index("username")
        idx          = {data['columns'].index(colname): colname for colname in data['columns'] }
        table_header = [html.Thead([html.Tr([html.Th(h) for h in data['columns']])])]
        table_rows   = [
            html.Tbody(
                       [html.Tr([html.Td(get_input(elem,f"{row[username_idx]}-{idx[row.index(elem)]}") if row.index(elem) != username_idx else elem) for elem in row]) for row in data['data']]
            )
        ]
        table = dbc.Table(
            table_header + table_rows,
            bordered=True,
            striped=True,
        )
        content = html.Div([table, dbc.Button("Send", color="success", className="me-1", id="send-btn")])
    return content
# dash callback that fetch the value of all input text field with their id beginning with "input-"

@callback(Output('sql-error', 'children'),
          [Input("send-btn", 'n_clicks')],
          [State({"type":"in-db", "index": ALL}, "value"), State({"type":"in-db", "index": ALL}, "id")]
    )
def display_output(clicks, values, ids):
    if clicks is None:
        raise PreventUpdate
    updates = {}
    for val, idx in zip(values, [i['index'] for i in ids]):
        username, colname = idx.split("-")
        if username not in updates: updates[username] = {}
        updates[username][colname] = val
    res = update_table(updates)
    return res

#------------------------------------------------------------------------------------
#-- Other functions
#------------------------------------------------------------------------------------
def get_input(text, id):
    full_id = {"type":"in-db", "index":id}
    return dbc.Input(value=text, type="text", id=full_id),
