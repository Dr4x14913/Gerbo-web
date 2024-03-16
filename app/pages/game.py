import dash
from dash.exceptions import PreventUpdate
from dash import html, dcc, callback, Input, Output, State, ALL, callback_context
import dash_bootstrap_components as dbc
from game_manager import get_all_puzzles, get_solutions, get_team, success_team_of_user, has_succeeded

dash.register_page(__name__)
COLS = ["name", "statement", "hint", "hint_number", "depends"]
# ------------- Page Components -------------------
layout = html.Div([
       html.Div([], id="game-content"),
       html.Div([], id="dummy")
])
# ------------ Callback functions ---------------
@callback(
    Output("game-content", "children"),
    [Input("dummy", "children")],
    [State("CURRENT_USER", "data")]
)
def display_game_callback(dummy, user):
    # if user not connected
    if (user is None) or (user == "None"):
        return html.Div(['You are nor log yet, please go ', dcc.Link("back home", href="home"), ' for loggin'])

    cards = to_html(COLS, user)
    return html.Div([] + cards)

@callback(
    Output("game-content", "children", allow_duplicate=True),
    [Input({'type':'btn-soluce', 'puzzle':ALL}, 'n_clicks')],
    [State("CURRENT_USER", "data"), State({'type':'in-soluce', 'puzzle':ALL}, 'value'), State({'type':'in-soluce', 'puzzle':ALL}, 'id')],
    prevent_initial_call=True
)
def soluce_callback(clicks, user, values, ids):
    if all(i is None for i in clicks):
         raise PreventUpdate
    ctx       = callback_context
    button_id = ctx.triggered_id
    puzzle_triggered = button_id['puzzle']
    suggested_soluce = [v for i,v in zip(ids, values) if i['puzzle']==puzzle_triggered][0]
    soluces          = get_solutions(puzzle_triggered)

    color = 'danger'
    msg   = 'Nice try but no ...'
    # if answer is in the list of good solutions
    if any([i for i in soluces if filter_string(i) == filter_string(suggested_soluce)]):
        status, msg = success_team_of_user(user, puzzle_triggered)
        if status == 0:
            color = 'success'
    alert = dbc.Alert(msg, color=color, duration=4000)
    cards = to_html(COLS, user)
    return html.Div([alert] + cards)



# ------------ Other functions ---------------
def filter_string(string):
    illegal_char_map = {
            "e": ['é', 'è', 'ë'],
            "a": ['à'],
            "": ["'", "%", "$", "*"]
            }
    string = string.lower()
    for letter, illegal in illegal_char_map.items():
        for c in illegal:
            string = string.replace(c,letter)

    # replace any blanck spaces more than 1 by one
    return " ".join(string.split())


def to_html(cols, user):
    cards     = []
    puzz_list = get_all_puzzles(cols)
    last      = -1
    for n, st, h, hi, d in zip(*puzz_list.values()):
        if n != last:
            # Create Card for puzzle
            card_body = dbc.CardBody([html.H4(n), html.H6(display(st), style={'text-align':'center'})])
            if not has_succeeded(get_team(user), n):
                card_body.children.append(dbc.Form(dbc.InputGroup([
                    dbc.Button(">", id={'type':'btn-soluce', 'puzzle':n}, type='submit'),
                    dbc.Input(placeholder="Solutionnnnn", id={'type':'in-soluce', 'puzzle':n})
                ])))
            card_body.children.extend([html.Br(), html.H6("Indices:")])

        # Display hints if they exists
        if h is not None:
            if has_succeeded(get_team(user), d):
                card_body.children.append(display(h))
            else:
                card_body.children.extend([dbc.Badge("Hint not available yet", color='info'), html.Br()])
        else:
            card_body.children.extend([dbc.Badge("No hint for this one", color='secondary'), html.Br()])


        if n != last:
            if has_succeeded(get_team(user), n):
                color = 'success'
            else:
                color = ''
            cards.append(dbc.Card([card_body], color=color))
            cards.append(html.Br())
            last = n
    return cards

def display(text):
    img_ext = ['png', 'jpg', 'jpeg']
    if any([i for i in img_ext if text.find(i) > -1]):
        return html.Img(src=text, style={'max-width':'100%'})
    else:
        return html.Div(text)
