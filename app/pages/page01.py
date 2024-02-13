import dash
from login_manager import get_current_user
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

#------------------------------------------------------------------------------------
dataframe = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['a', 'b', 'c']})
dbc_table = html.Table([
    html.Thead(
        html.Tr([html.Th(col) for col in dataframe.columns])
        ),
    html.Tbody([
        html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(len(dataframe))
        ])
    ], className='table')

content = dbc.Container(dbc_table, fluid=True)


#------------------------------------------------------------------------------------
dash.register_page(__name__)

layout = html.Div([
    html.H1(f'This is our {__name__} page', id='title'),
    html.Div([], id='resp'),
    html.Br(),
])

#------------------------------------------------------------------------------------
@callback(
    Output("resp", "children"),
    [Input("title", "value")],
)
def tt(u):
    user = get_current_user()
    if user is not None:
        return content
    else:
        return f'You are nor log yet, please go {dcc.Link("back home", href="home")} for loggin'
