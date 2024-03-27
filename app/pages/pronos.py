import dash
from dash import html, dcc, callback, Input, Output, State, ALL, callback_context
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from pronos_manager import get_pronos, get_choices, get_label, set_prono_res
from backoffice_manager import get_disabled_pages
#------------------------------------------------------------------------------------
dash.register_page(__name__)

phantom_style    = {'display': 'none'}
phantom_children = [
    # html.Div(id='pronos-content',        style=phantom_style)
]


layout = html.Div([
    html.Div(phantom_children, id='pronos-content')
])


#------------------------------------------------------------------------------------
@callback(
    Output("pronos-content", "children"),
    [Input("pronos-content", "children")],
    [State("CURRENT_USER", "data")]
)
def display_pronos(dummy, user):
    # if user not connected
    if (user is None) or (user == "None"):
        return html.Div(['You are nor log yet, please go ', dcc.Link("back home", href="home"), ' for loggin'])

    if str(__name__).split('.')[-1] in get_disabled_pages():
        return html.Div(['You are not allowed to be here, please go away before Didjo la canaille te botte le derch'])

    res_div   = html.Div(id='pronos-res')
    pronos_in = []
    for p in get_pronos():
        label  = dbc.Label(f"Vote pour: {get_label(p)}")
        select = dbc.Select(
                id={'type':'pronos-in','prono':p},
                options=[{"label": i, "value": i} for i in get_choices(p)]
        )
        btn    = dbc.Button("Send", id={'type':'pronos-btn-send', 'prono':p})
        pronos_in.append(html.Div([label, select, btn]))
    return pronos_in + [res_div]
#------------------------------------------------------------------------------------
@callback(
    Output("pronos-res", "children"),
    [Input({'type':'pronos-btn-send', 'prono':ALL}, "n_clicks")],
    [State({'type':'pronos-in','prono':ALL}, "value"), State({'type':'pronos-in','prono':ALL}, "id"), State("CURRENT_USER", "data")]
)
def set_prono(clicks, input_values, input_ids, user):
    if all(i is None for i in clicks):
        raise PreventUpdate
    ctx       = callback_context
    button_id = ctx.triggered_id
    prono     = button_id['prono']
    value = input_values[[i['prono'].lower() for i in input_ids].index(prono.lower())]

    return set_prono_res(prono, user, value)


