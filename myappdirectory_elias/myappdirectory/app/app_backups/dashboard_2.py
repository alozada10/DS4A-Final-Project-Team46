import matplotlib.pyplot as plt
import numpy as np
import base64
import datetime
import dash
import io
import pandas as pd
import dash_table
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import os

UPLOAD_DIRECTORY = "C:/pruebas_2345"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
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
            'top': '50%',
            'left': '7.5%',
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

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    
    #Para guardar archivo en disco
    data = contents.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(base64.decodebytes(data))


    req_path = UPLOAD_DIRECTORY + "/" + filename

    df = pd.read_csv(req_path)
    df.columns=["Pagina","Probabilidad"]

    #fig = px.bar(df, x="Pagina", y="Probabilidad")
    
    plt.figure(figsize=(10,10))
    
    fig = go.Figure(go.Bar(
            x=df["Probabilidad"],
            y=(df["Pagina"].astype(str)),
            orientation='h'))
    
    fig.update_layout(
    title={
        'text': "Páginas más probables",
        'y':0.8,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    autosize=False,
    width=300,
    height=300,
    xaxis=dict(
        title_text="%Probabilidad",
        tickmode="array",
        titlefont=dict(size=15),
        ),
    yaxis=dict(
        title_text="Página",
        tickmode="array",
        titlefont=dict(size=15),
        tickformat=',d'
        ),
)
    
    return dcc.Graph(figure=fig)

@app.callback(Output('output-upload', 'children'),
              [Input('Procesar-button', 'n_clicks')],
              [State('upload-file', 'contents'),
               State('upload-file', 'filename'),
               State('upload-file', 'last_modified')])
def update_output(click, list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
    
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)