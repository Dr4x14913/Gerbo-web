import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from profiles_list import get_profile, get_avatar
# Pretty html table using dbc from simple python dict such as {"Etat":"Probablement nu","Ivre":"oui",}



#------------------------------------------------------------------------------------
dash.register_page(__name__)

layout = html.Div([
    html.Div(id='profile-content'),
    html.Br(),
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

    data  = get_profile(user)
    image = get_avatar(user)
    component = gen_component(data, image)
    return component
    

def gen_component(data, image):
    component = html.Div((
        [html.Img(src=image, id='avatar')] + # avatar image
        [ # feature list
            html.Div([
                html.Div(key, className="feature-label"), 
                html.Div(":", className="feature-separator"),
                html.Div(value, className="feature-value"),
            ], className="feature")

            for key, value in data.items()
        ]
    ), id="profile-informations")
    return component
