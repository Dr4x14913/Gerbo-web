import dash
from dash.exceptions import PreventUpdate
from dash import html, dcc, callback, Input, Output, State, ALL, callback_context
import dash_bootstrap_components as dbc
import pandas as pd
from backoffice_manager import get_db_data_as_df, update_table, insert_row, del_row

tables = {
        "users": {
            "cols": ["username", "display_name", "team", "avatar_name"],
            "cond": "username != 'admin'",
            "cols_create": ["username", "password", "display_name", "team", "avatar_name"],
            },
        "teams": {
            "cols": ["name", "color"],
            "cond": "1",
            "cols_create": ["name", "color"],
           },
        "pronos": {
            "cols": ["name", "choices", "label"],
            "cond": "1",
            "cols_create": ["name", "choices", "label"],
            },
        "pronosResults": {
            "cols": ["id", "prono_name", "username", "vote", "time"],
            "cond": "1",
            "cols_create": [],
            },
        "puzzles": {
            "cols": ["name", "solution", "statement"],
            "cond": "1",
            "cols_create": ["name", "solution", "statement"]
            },
        "puzzles_hints": {
            "cols": ["id", "puzzle", "hint", "hint_number", "depends"],
            "cond": "1",
            "cols_create": ["puzzle", "hint", "hint_number", "depends"],
            },
        "puzzles_success": {
            "cols": ["id", "puzzle", "team"],
            "cond": "1",
            "cols_create": ["puzzle", "team"],
            },
        "disabled_pages": {
            "cols": ["page"],
            "cond": "1",
            "cols_create": ["page"],
            },
        "schedule": {
            "cols": ["id", "day", "hour", "activity"],
            "cond": "1",
            "cols_create": ["day", "hour", "activity"],
            },
        "menus": {
            "cols": ["id", "day", "time", "menu", "orga"],
            "cond": "1",
            "cols_create": ["day", "time", "menu", "orga"],
            },
        }

#------------------------------------------------------------------------------------
dash.register_page(__name__)

# Define phantom children (components that will be used in callbacks but aren't displayed yet)
phantom_style    = {'display': 'none'}
phantom_children = [
    dbc.Tabs(id="card-tabs",        style=phantom_style),
    dbc.Modal(id="add-row-modal",   style=phantom_style),
    html.Div(id='sql-error',        style=phantom_style),
    dbc.CardBody(id='card-content', style=phantom_style),
]

modal = html.Div(
    [
        dbc.Modal(
            [
            ],
            id="add-row-modal",
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
    ]
)
content = [card, modal]

layout = html.Div([
    html.Div(phantom_children, id='backoffice-content'),
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
            content.append(html.H4(dbc.Badge(t)))
            cols = tables[t]["cols"]
            cond = tables[t]["cond"]
            content.append(dbc.Table.from_dataframe(get_db_data_as_df(t, cols, cond), striped=True, bordered=True, hover=True))
    else:
        for t in tables:
            cols           = tables[t]["cols"]
            cond           = tables[t]["cond"]
            table_w_inputs = gen_table_with_inputs(t, cols, cond)
            form = dbc.Form([
                html.H4(dbc.Badge(t)),
                table_w_inputs,
                dbc.Button("Send", color="success", className="me-1", id={"type":"send-db", "totable":f"{t}"}),
            ])
            content.append(form)
    return html.Div(content)

#------------------------------------------------------------------------------------
# This callback update the database based on what contain the input fields
@callback(Output('sql-error', 'children'),
          [Input({"type":"send-db", "totable": ALL}, 'n_clicks')],
          [State({"type":"in-db-txt", "table": ALL, "row":ALL, "col":ALL}, "value"), State({"type":"in-db-txt", "table": ALL, "row":ALL, "col":ALL}, "id")]
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

#------------------------------------------------------------------------------------
@callback([Output("add-row-modal", "is_open"),Output("add-row-modal", "children")],
          [Input({"type":"openmodal-btn", "table":ALL}, 'n_clicks')],
          [State("add-row-modal", "is_open")],
          prevent_initial_call=True
    )
def display_modal_callback(clicks_add, is_open):
    if clicks_add.count(None) == len(clicks_add):
        raise PreventUpdate
    ctx       = callback_context
    button_id = ctx.triggered_id
    table2add = button_id["table"]
    columns   = tables[table2add]["cols_create"]

    table_header = [html.Thead([html.Tr([html.Th(h) for h in columns])])]
    table_rows   = [
        html.Tbody(
            [html.Tr([html.Td(get_input(col,"add-db-txt",table2add,"new",col, place_holder=True)) for col in columns])]
        )
    ]
    table_full = dbc.Table(
        table_header + table_rows,
        bordered=True,
        striped=True,
    )
    modal_content = html.Div([
        dbc.ModalHeader(dbc.ModalTitle(f"Adding one row to {table2add}")),
        dbc.ModalBody(
            dbc.Form([
                table_full,
                dbc.Button("Update", id={"type":"add-db-btn", "table":table2add}, color="primary")
            ])
        ),
    ])
    return True, modal_content
#------------------------------------------------------------------------------------
@callback([Output("add-row-modal", "is_open", allow_duplicate=True), Output("sql-error", "children", allow_duplicate=True), Output("card-tabs", "active_tab", allow_duplicate=True)],
        [Input({"type":"add-db-btn", "table": ALL}, 'n_clicks'), ],
        [State({"type":"add-db-txt", "table": ALL, "row":"new", "col":ALL}, 'value'), State({"type":"add-db-txt", "table":ALL,"row":"new", "col":ALL}, 'id')],
       prevent_initial_call=True )
def add_in_table(clicks, input_txt_values, input_txt_ids):
    if clicks.count(None) == len(clicks):
        raise PreventUpdate
    ctx       = callback_context
    button_id = ctx.triggered_id
    table2add = button_id["table"]

    values   = []
    colsname = []
    for v, i in zip(input_txt_values, input_txt_ids):
        if i['table'] == table2add:
            values.append(v)
            colsname.append(i['col'])

    return False, insert_row(table2add, colsname, values), "tab-edit"


#------------------------------------------------------------------------------------
@callback([Output("sql-error", "children", allow_duplicate=True), Output("card-tabs", "active_tab", allow_duplicate=True)],
        [Input({'type':'del-db-btn', 'row':ALL, 'col':ALL, 'table': ALL}, 'n_clicks')],
          prevent_initial_call=True,
        )
def del_row_callback(clicks):
    if clicks.count(None) == len(clicks):
        raise PreventUpdate
    ctx       = callback_context
    button_id = ctx.triggered_id
    table     = button_id["table"]
    row       = button_id["row"]
    col       = button_id["col"]
    return del_row(table, row, col), 'tab-edit'

#------------------------------------------------------------------------------------
#-- Other functions
#------------------------------------------------------------------------------------
def get_input(text, type_, table, row, col, place_holder=False):
    full_id = {"type":type_, "table":table, "row":row, "col":col}
    if not place_holder:
        return dbc.Input(value=text, type="text", id=full_id),
    return dbc.Input(placeholder=text, type="text", id=full_id),


# Takes a table name, a list of columns and a sql where condition, and return a html table
# with input text field pre-filled with databse table content
def gen_table_with_inputs(table, cols, cond="1"):
    data         = get_db_data_as_df(table, cols, cond).to_dict('split')
    idx          = {data['columns'].index(colname): colname for colname in data['columns'] }
    table_header = [html.Thead([html.Tr([html.Th(h) for h in data['columns']] + [html.Th()])])]
    last_row = [html.Tr([html.Td(dbc.Button(html.I(className="bi bi-plus-circle"), type='button', color="warning", id={"type":"openmodal-btn", "table":table}))])]
    table_rows   = [
        html.Tbody([
            html.Tr([
                html.Td(get_input(elem,"in-db-txt",table,row[0],idx[row.index(elem)]) if row.index(elem) != 0 else elem)
                for elem in row ] + [html.Td(dbc.Button(html.I(className='bi bi-x-square'), color='danger', type='button', id={'type':'del-db-btn', 'row':row[0], 'col':idx[0], 'table':table}), className='text-center')]
                )
            for row in data['data'] ] + last_row
        )
    ]
    table = dbc.Table(
        table_header + table_rows,
        bordered=True,
        striped=True,
    )
    return table
