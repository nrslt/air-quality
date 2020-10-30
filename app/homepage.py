"""The following is dedicated to elements of the homepage.
"""
# ------------------------------------------------------------------------------
# Imports

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from mainmap import build_main_map

from navbar import Navbar

# instantiating a navigation bar object
nav = Navbar()

# creating the main map fig object
main_map_fig = build_main_map()

body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("Airqual project"),
                     html.P(
                         """\
This app is a demo project that aims at displaying historical and predicted\
air quality measures."""
                           ),
                           dbc.Button("View details", color="secondary"),
                   ],
                  md=4,
               ),
              dbc.Col(
                 [
                     html.H2("Air quality historical data"),
                     dcc.Graph(
                         id='main_map',
                         figure=main_map_fig
                            ),
                        ],
                        md=8
                     ),
                ]
            )
       ],
className="mt-4",
)

def Homepage():
    layout = html.Div([
    nav,
    body
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Homepage()
if __name__ == "__main__":
    app.run_server()


