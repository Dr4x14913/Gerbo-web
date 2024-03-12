import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from profiles_list import get_profile, get_avatar, get_display_name, set_display_name, set_password
from dash.exceptions import PreventUpdate
#------------------------------------------------------------------------------------
dash.register_page(__name__)

phantom_style    = {'display': 'none'}
phantom_children = [
    html.Div(id='change-name-res',        style=phantom_style)
]


layout = html.Div([
    html.Div(phantom_children, id='profile-content')
])


#------------------------------------------------------------------------------------
@callback(
    Output("profile-content", "children"),
    [Input("profile-content", "children")],
    [State("CURRENT_USER", "data")]
)
def display_profile_callback(dummy, user):
    # if user not connected
    if (user is None) or (user == "None"):
        return html.Div(['You are nor log yet, please go ', dcc.Link("back home", href="home"), ' for loggin'])

    image       = get_avatar(user)
    actual_name = get_display_name(user)
    component   = gen_component(user, image)
    change_name = gen_fade_change_name(actual_name)
    change_pswd = gen_fade_change_pswd()

    return html.Div([component, change_name, change_pswd])
#------------------------------------------------------------------------------------
@callback(
    Output("fade-change-pswd", "is_in"),
    [Input("fade-change-pswd-btn", "n_clicks")],
    [State("fade-change-pswd", "is_in")],
)
def toggle_fade_pswd(clicks, is_in):
    if not clicks:
        # Button has never been clicked
        return False
    return not is_in
#------------------------------------------------------------------------------------
@callback(
    Output("fade-change-name", "is_in"),
    [Input("fade-change-name-btn", "n_clicks")],
    [State("fade-change-name", "is_in")],
)
def toggle_fade_display_name(clicks, is_in):
    if not clicks:
        # Button has never been clicked
        return False
    return not is_in

#------------------------------------------------------------------------------------
@callback(
    Output('change-pswd-res', 'children'),
    [Input("pswd-btn", "n_clicks")],
    [State("CURRENT_USER", "data"), State("pswd-in", "value")],
    prevent_initial_call=True
)
def change_pswd(clicks, user, pswd):
    if not clicks:
        raise PreventUpdate
    if set_password(user, pswd): # Return 1 when sql error occured
        alert = dbc.Alert("Something went wrong, please try again later", color='danger', duration=4000)
        return alert
    else:
        alert = dbc.Alert("Password successfully changed", color='success', duration=4000)
        return alert # False to close the fade

#------------------------------------------------------------------------------------
@callback(
    Output('change-name-res', 'children'),
    [Input("display-name-btn", "n_clicks")],
    [State("CURRENT_USER", "data"), State("display-name", "value")],
    prevent_initial_call=True
)
def change_display_name(clicks, user, name):
    if not clicks:
        raise PreventUpdate
    if set_display_name(user, name): # Return 1 when sql error occured
        alert = dbc.Alert("Something went wrong, please try again later", color='danger', duration=4000)
        return alert

    alert = dbc.Alert("Name successfully changed", color='success', duration=4000)
    return alert # False to close the fade


#-----------------------------------------------------------------------------------
@callback(
    Output("profile-table", "children"),
    [Input("change-name-res", "children")],
    [State("CURRENT_USER", "data")],
)
def update_table(dummy, user):
    return gen_table(user)

#------------------------------------------------------------------------------------
def gen_fade_change_pswd():
    fade = html.Div(
        [
            dbc.Button(
                "Change password", id="fade-change-pswd-btn", className="mb-3", n_clicks=0
            ),
            dbc.Fade(
                dbc.Card(
                    dbc.CardBody(
                        dbc.Form([
                            dbc.InputGroup([
                                dbc.Input(type='password', id='pswd-in', placeholder="New password"),
                                dbc.Button(html.I(className='bi bi-check-circle-fill'), id='pswd-btn'),
                            ])
                        ])
                    )
                ),
                id="fade-change-pswd",
                is_in=False,
                appear=False,
            ),
            html.Div([], id='change-pswd-res')
        ]
    )
    return fade
#------------------------------------------------------------------------------------
def gen_fade_change_name(display_name):
    fade = html.Div(
        [
            dbc.Button(
                "Change display name", id="fade-change-name-btn", className="mb-3", n_clicks=0
            ),
            dbc.Fade(
                dbc.Card(
                    dbc.CardBody(
                        dbc.Form([
                            dbc.InputGroup([
                                dbc.Input(value=display_name, id='display-name'),
                                dbc.Button(html.I(className='bi bi-check-circle-fill'), id='display-name-btn'),
                            ])
                        ])
                    )
                ),
                id="fade-change-name",
                is_in=False,
                appear=False,
            ),
            html.Div([], id='change-name-res')
        ]
    )
    return fade

def gen_table(user):
    data  = get_profile(user)

    rows = [html.Tr([html.Td(key), html.Td(value)]) for key, value in data.items()]
    table_body = [html.Tbody(rows)]
    table = dbc.Table(table_body, bordered=True, id="profile-table")

    return table

def gen_component(user, image):
    table = gen_table(user)

    component = html.Div((
        [html.Img(src=image, id='avatar')] + # avatar image
        [table]
    ), id="profile-informations")
    return component
