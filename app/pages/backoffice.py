import dash
from dash.exceptions import PreventUpdate
from dash import html, dcc, callback, Input, Output, State, ALL, callback_context
import dash_bootstrap_components as dbc
import pandas as pd
from backoffice_manager import get_db_data_as_df, update_table

tables = {
        "users": {
            "cols": ["username", "display_name", "team", "avatar_name"],
            "cond": "username != 'admin'",
            },
        "teams": {
            "cols": ["name", "color"],
            "cond": "1",
            }
        }

#------------------------------------------------------------------------------------
dash.register_page(__name__)

modal = html.Div(
    [
        dbc.Modal(
            [
            ],
            id="modal",
            is_open=False,
        ),
    ]
)
card =  dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="Show db", tab_id="tab-show"),
                    dbc.Tab(label="Modify db", tab_id="tab-edit"),
                ],
                id="card-tabs",
                active_tab="tab-show",
            )
        ),
        dbc.CardBody(html.P(id="card-content", className="card-text")),
       html.Br(),
       html.Div([], id="sql-error", className="danger"),
       html.Div([], id="add-error", className="danger"),
    ]
)
content = [card, modal]
layout = html.Div([
    html.Div([], id='backoffice-content'),
])

#------------------------------------------------------------------------------------
#-- Callbacks
#------------------------------------------------------------------------------------
# This callback either display an error or the real content of the page depending on
# the user you are log with
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

#------------------------------------------------------------------------------------
# This callback display the content of the database as boostrap tables. Two modes
# are availables, the display mode that just display the databse content and the
# Edit mode, that allow the admin user to change data.
@callback(
    Output("card-content", "children"),
    [Input("card-tabs", "active_tab")],
)
def display_tables_callback(tab):
    content = []
    if tab == "tab-show":
        for t in tables:
            cols = tables[t]["cols"]
            cond = tables[t]["cond"]
            content.append(dbc.Table.from_dataframe(get_db_data_as_df(t, cols, cond), striped=True, bordered=True, hover=True))
    else:
        for t in tables:
            cols = tables[t]["cols"]
            cond = tables[t]["cond"]
            tmp = gen_table_with_inputs(t, cols, cond)
            content.append(html.Div([tmp, dbc.Button("Send", color="success", className="me-1", id={"type":"send-db", "totable":f"{t}"})]))
            content.append(html.Br())
    return html.Div(content)

#------------------------------------------------------------------------------------
# This callback update the database based on what contain the input fields
@callback(Output('sql-error', 'children'),
          [Input({"type":"send-db", "totable": ALL}, 'n_clicks')],
          [State({"type":"in-db", "table": ALL, "row":ALL, "col":ALL}, "value"), State({"type":"in-db", "table": ALL, "row":ALL, "col":ALL}, "id")]
    )
def update_tables_callback(clicks, values, ids):
    if all(i is None for i in clicks):
        raise PreventUpdate
    ctx       = callback_context
    button_id = ctx.triggered_id

    table2update    = button_id["totable"]
    main_col        = tables[table2update]["cols"][0]
    values_filtered = []
    ids_filtered    = []
    for i,v in zip(ids, values):
        if i['table'] == table2update:
            values_filtered.append(v)
            ids_filtered.append([i['row'], i['col']])
    updates = {}
    for val, idx in zip(values_filtered, ids_filtered):
        cond, colname = idx
        if cond not in updates: updates[cond] = {}
        updates[cond][colname] = val
    res = update_table(table2update, updates, main_col)
    return res

@callback([Output("modal", "is_open"),Output("modal", "children")],
          [Input({"type":"add-db", "table":ALL}, 'n_clicks')],
          [State("modal", "is_open")],
          prevent_initial_call=True
    )
def add_line_callback(clicks_add, is_open):
    if clicks_add.count(None) == len(clicks_add):
        raise PreventUpdate
    ctx       = callback_context
    button_id = ctx.triggered_id
    table2add = button_id["table"]
    modal_content = html.Div([
        dbc.ModalHeader(dbc.ModalTitle(table2add)),
        dbc.ModalBody("This is the content of the modal"),
        dbc.ModalFooter(),
    ])
    return True, modal_content
#------------------------------------------------------------------------------------
#-- Other functions
#------------------------------------------------------------------------------------
def get_input(text, table, row, col):
    full_id = {"type":f"in-db", "table":table, "row":row, "col":col}
    return dbc.Input(value=text, type="text", id=full_id),

# Takes a table name, a list of columns and a sql where condition, and return a html table
# with input text field pre-filled with databse table content
def gen_table_with_inputs(table, cols, cond="1"):
    data         = get_db_data_as_df(table, cols, cond).to_dict('split')
    idx          = {data['columns'].index(colname): colname for colname in data['columns'] }
    table_header = [html.Thead([html.Tr([html.Th(h) for h in data['columns']])])]
    last_row = [html.Tr([html.Td(dbc.Button(html.I(className="bi bi-plus-circle"), color="warning", id={"type":"add-db", "table":table}))])]
    table_rows   = [
        html.Tbody(
            [html.Tr([html.Td(get_input(elem,table,row[0],idx[row.index(elem)]) if row.index(elem) != 0 else elem) for elem in row]) for row in data['data']] +
            last_row
        )
    ]
    table = dbc.Table(
        table_header + table_rows,
        bordered=True,
        striped=True,
    )
    return table
