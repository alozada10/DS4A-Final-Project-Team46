#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

#Dash Bootstrap Components
import dash_bootstrap_components as dbc 

#Recall app
from app import app

upload = html.Div([
    #Create de upload buttom
    dcc.Upload(
        id='upload-file',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Seleccionar Archivo')
        ]),
        style={
            'width': '20%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '2px',
            'borderStyle': 'solid',
            'borderRadius': '8px',
            'textAlign': 'center',
            #https://www.w3schools.com/css/css_background.asp
            #https://htmlcolorcodes.com/es/
            'background-color': '#F8F6F6',
            'color': '#717272',
            'border-color': '#717272',
            'position': 'absolute',
            'top': '60%',
            'left': '12%',
            'font-family': 'Arial, Helvetica, sans-serif',
            'font-style': 'normal',
            'font-size': '16px',
            'font-weight': 'normal',
            'vertical-align': 'middle'
       },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-upload'),
    #Create Execute buttom
    html.Div([
        html.Button('Procesar', id='Procesar-button', n_clicks = 0 ,
       style={
            'width': '20%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '2px',
            'borderStyle': 'solid',
            'borderRadius': '8px',
            'textAlign': 'center',
            #https://www.w3schools.com/css/css_background.asp
            #https://htmlcolorcodes.com/es/
            'background-color': '#ABD7A6',
            'color': '#0D5905',
            'border-color': '#0D5905',
            'position': 'absolute',
            'top': '70%',
            'left': '7.5%',
            'font-family': 'Arial, Helvetica, sans-serif',
            'font-style': 'normal',
            'font-size': '16px',
            'font-weight': 'normal',
            'text-transform': 'capitalize',
            'vertical-align': 'middle'
       }, 
     ),
     html.Div(id='output-Procesar')   
   ])
])