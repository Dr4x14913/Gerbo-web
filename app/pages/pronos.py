import dash
from dash import html, dcc, callback, Input, Output, State, ALL, callback_context
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
from pronos_manager import get_pronos, get_choices, get_label, set_prono_res, get_last_vote, get_prono_count
from backoffice_manager import get_disabled_pages
#------------------------------------------------------------------------------------
dash.register_page(__name__)

phantom_style    = {'display': 'none'}
phantom_children = [
    # html.Div(id='pronos-content',        style=phantom_style)
]


layout = html.Div([
    html.Div(phantom_children, id='pronos-content', style={'width':'100vw'}, className='px-1')
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

    return gen_input_and_graphs(user)

#------------------------------------------------------------------------------------
@callback(
    [Output("pronos-res", "children"), Output("pronos-content", "children", allow_duplicate=True)],
    [Input({'type':'pronos-btn-send', 'prono':ALL}, "n_clicks")],
    [State({'type':'pronos-in','prono':ALL}, "value"), State({'type':'pronos-in','prono':ALL}, "id"), State("CURRENT_USER", "data")],
    prevent_initial_call = True
)
def set_prono(clicks, input_values, input_ids, user):
    if all(i is None for i in clicks):
        raise PreventUpdate
    ctx       = callback_context
    button_id = ctx.triggered_id
    prono     = button_id['prono']
    value = input_values[[i['prono'].lower() for i in input_ids].index(prono.lower())]
    return set_prono_res(prono, user, value), gen_input_and_graphs(user)

#------------------------------------------------------------------------------------
def gen_input_and_graphs(user):
    graphs    = []
    pronos_in = []
    for p in get_pronos():
        choices   = get_choices(p)
        label     = dbc.Label(f"Vote pour: {get_label(p)}")
        last_vote = get_last_vote(p, user)
        if choices[0] == '*':
            select = dbc.Input(id={'type':'pronos-in','prono':p}, placeholder=last_vote)
        else:
            select = dbc.Select(
                    id={'type':'pronos-in','prono':p},
                    options=[{"label": i, "value": i} for i in get_choices(p)],
                    value = last_vote
            )
        btn    = dbc.Button("Send", id={'type':'pronos-btn-send', 'prono':p}, className='m-1')
        pronos_in.append(html.Div([label, select, btn]))

        votes = get_prono_count(p)
        graphs.append(
            dcc.Graph(
                figure= go.Figure(
                    data=go.Bar(
                    x = list(votes.keys()),
                    y = list(votes.values()),
                    ),
                    layout = dict(
                        title = get_label(p),
                        template ='plotly_dark'
                    ),
                ),
                className='my-1', style={'borderRadius': '15px', 'overflow': 'hidden'}
            )
        )
    return html.Div(pronos_in + graphs + [html.Div(id='pronos-res')])
