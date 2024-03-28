import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output, State, ALL
from dash.exceptions import PreventUpdate
from backoffice_manager import get_disabled_pages, log
from planning_manager import get_activities, get_days, get_menus
#------------------------------------------------------------------------------------
dash.register_page(__name__)

phantom_style    = {'display': 'none'}
phantom_children = [
]


layout = html.Div([
    html.Div(phantom_children, id='planning-content'),
    html.Div(id={'type':"other",'id':'y'}),
    html.Div(id={'type':"other",'id':'d'}),
    html.Div(id="other"),
])


#------------------------------------------------------------------------------------
@callback(
    Output("planning-content", "children"),
    [Input("planning-content", "children")],
    [State("CURRENT_USER", "data")]
)
def display_planning_callback(dummy, user):
    if str(__name__).split('.')[-1] in get_disabled_pages():
        return html.Div(['You are not allowed to be here, please go away before Didjo la canaille te botte le derch'])
    return get_planning_content()

#------------------------------------------------------------------------------------
@callback(
    Output({'type':"card-content",'day':ALL}, "children", allow_duplicate=True),
    [Input({'type':'tab', 'day':ALL}, "active_tab"), Input({'type':'tab', 'day':ALL}, "id")],
    prevent_initial_call=True
)
def update_tabs_callback(active_tabs, tabs_id):
    content_list = []
    for index, tab in zip(range(len(active_tabs)), active_tabs):
        if tab == "schedule":
            content_list.append(get_schedule(tabs_id[index]['day']))
        else:
            content_list.append(get_meals(tabs_id[index]['day']))
    return content_list

#------------------------------------------------------------------------------------
def get_planning_content():
    plan = []
    for day in get_days():
        daycard = dbc.Card([
            dbc.CardHeader([
                html.H4(day),
                dbc.Tabs([
                    dbc.Tab(label="Planning", tab_id=f"schedule"),
                    dbc.Tab(label="Repas", tab_id=f"repas"),
                    ],
                active_tab='schedule',
                id={'type':'tab','day':day.lower()}
                )
            ]),
            dbc.CardBody(
                get_schedule(day),
                id={'type':'card-content','day':day},
            )
        ])
        plan.append(daycard)
        plan.append(html.Br())

    return plan

def get_schedule(day):
    activities = []
    for time, activity in get_activities(day):
        activities.append(
            html.Tr([
                html.Td(dbc.Badge(time, color="info")),
                html.Td(activity),
            ])
        )

    return dbc.Table(html.Tbody(activities), bordered=True, hover=True, striped=True,)

def get_meals(day):
    menus = []
    for time, menu, orga in get_menus(day):
        menus.append(
            html.Tr([
                html.Td(dbc.Badge(time, color="info")),
                html.Td(menu),
                dbc.Badge(orga, color="danger", pill=True, className="position-absolute top-0 start-100 translate-middle")
            ], className="position-relative")
        )

    return dbc.Table(html.Tbody(menus), bordered=True, hover=True, striped=True,)
