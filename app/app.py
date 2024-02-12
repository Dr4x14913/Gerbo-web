import dash
from dash import dcc
from dash import html
import mysql.connector
from mysql.connector import Error

MYSQL_USER     = 'user'
MYSQL_PASSWORD = 'password'
MYSQL_DATABASE = 'website'

#Establish the connection to MariaDB
try:
    cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host='db', database=MYSQL_DATABASE)
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    print(f"Something went wrong: {err}")
    exit(1)
else:
    print("Connection successful!")

# SQL query
query = "SHOW TABLES;"

# Execute the query and fetch data
cursor.execute(query)
data = cursor.fetchall()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Welcome to our web page!', style={'textAlign': 'center'}),
])
app.layout = html.Div([
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [row[0] for row in data], 'y': [row[1] for row in data], 'type': 'bar',
'name': 'Your Data'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
