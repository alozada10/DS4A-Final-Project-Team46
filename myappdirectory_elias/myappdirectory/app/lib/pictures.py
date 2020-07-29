#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html


#Dash Bootstrap Components
import dash_bootstrap_components as dbc 

#Data
import json
from datetime import datetime as dt

#Recall app
from app import app



####################################################################################
# Add the DS4A_Img
####################################################################################

DS4A_Img=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("ds4a-cnc.jpg"),
                    id="ds4a-image",
                )
            ],className='ds4a-style-image'
        )

####################################################################################
# Add the Line_Img
####################################################################################

Line_Img=html.Div(
            children=[
                html.Img(
                    src=app.get_asset_url("line.jpg"),
                    id="line-image",
                )
            ],className='line-style-image'
        )
