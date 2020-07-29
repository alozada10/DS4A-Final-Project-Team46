#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html


#Dash Bootstrap Components
import dash_bootstrap_components as dbc 

#Recall app
from app import app

title_backgroung=html.Div(
	children=[html.H1("")],
	id="title_backgroung",
style={
            'width': '70%',
            'height': '80px',
            'borderRadius': '8px',
            'textAlign': 'left',
            'background-color': '#434545',
            'position': 'absolute',
            'top': '5%',
            'left': '5%',
            'resize': 'none'
            },
      )

title_text=html.Div(
	children=[html.H1("Lector de Pliegos")],
	id="title_text",
style={
            'width': '70%',
            'height': '80px',
            'textAlign': 'left',
            #https://www.w3schools.com/css/css_background.asp
            #https://htmlcolorcodes.com/es/
            'color': 'white',
            'position': 'absolute',
            'top': '6.7%',
            'left': '6.7%',
            'font-family': 'Arial, Helvetica, sans-serif',
            'font-style': 'normal',
            'font-size': '20px',
            'font-weight': 'bold',
            'vertical-align': 'center',
            'resize': 'none'
       },)

texto1=html.Div(
	children=[html.H3("En esta herramienta usted podrá cargar un archivo pdf con licitaciones, para que se extraigan los perfiles requeridos en el proyecto.")],
	id="texto1",
style={
            'width': '70%',
            'height': '80px',
            'textAlign': 'left',
            #https://www.w3schools.com/css/css_background.asp
            #https://htmlcolorcodes.com/es/
            'color': 'black',
            'position': 'absolute',
            'top': '17%',
            'left': '6.7%',
            'font-family': 'Arial, Helvetica, sans-serif',
            'font-style': 'normal',
            'font-size': '12px',
            'font-weight': 'normal',
            'vertical-align': 'center',
            'resize': 'none'
       },)

texto2=html.Div(
	children=[html.H3("Procesamiento de datos")],
	id="texto2",
style={
            'width': '28%',
            'height': '30px',
            'textAlign': 'center',
            #https://www.w3schools.com/css/css_background.asp
            #https://htmlcolorcodes.com/es/
            'color': 'black',
            'position': 'absolute',
            'top': '33%',
            'left': '6.7%',
            'font-family': 'Arial, Helvetica, sans-serif',
            'font-style': 'normal',
            'font-size': '12px',
            'font-weight': 'normal',
            'vertical-align': 'center',
            'resize': 'none',
            'text-decoration': 'underline'
       },)

texto3=html.Div(
	children=[html.H5("Nota: Recuerde que el archivo debe ser “.pdf” y las páginas deben estar en sentido vertical")],
	id="texto3",
style={
            'width': '30%',
            'height': '30px',
            'textAlign': 'left',
            #https://www.w3schools.com/css/css_background.asp
            #https://htmlcolorcodes.com/es/
            'color': 'black',
            'position': 'absolute',
            'top': '42%',
            'left': '6.7%',
            'font-family': 'Arial, Helvetica, sans-serif',
            'font-style': 'normal',
            'font-size': '6px',
            'font-weight': 'normal',
            'vertical-align': 'center',
            'resize': 'none'
        },)

texto4=html.Div(
	children=[html.H3("Resultados")],
	id="texto4",
style={
            'width': '28%',
            'height': '30px',
            'textAlign': 'center',
            #https://www.w3schools.com/css/css_background.asp
            #https://htmlcolorcodes.com/es/
            'color': 'black',
            'position': 'absolute',
            'top': '33%',
            'left': '55%',
            'font-family': 'Arial, Helvetica, sans-serif',
            'font-style': 'normal',
            'font-size': '12px',
            'font-weight': 'bold',
            'vertical-align': 'center',
            'resize': 'none',
            'text-decoration': 'underline'
        },)

texto5=html.Div(
	children=[html.H5("El archivo se ha procesado exitosamente")],
	id="texto5",
style={
            'width': '28%',
            'height': '30px',
            'textAlign': 'center',
            #https://www.w3schools.com/css/css_background.asp
            #https://htmlcolorcodes.com/es/
            'color': 'black',
            'position': 'absolute',
            'top': '42%',
            'left': '55%',
            'font-family': 'Arial, Helvetica, sans-serif',
            'font-style': 'normal',
            'font-size': '12px',
            'font-weight': 'bold',
            'vertical-align': 'center',
            'resize': 'none'
        },)