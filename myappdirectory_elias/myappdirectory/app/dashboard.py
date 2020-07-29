# local imports
from jobs.tender_profile_extractor import main as main_back
from jobs.tender_profile_extractor import settings
from utils import file_manager as fm
from utils import plot_info as pi

from dash.dependencies import Input, Output, State

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import os
import pandas as pd
import base64
from app import app

UPLOAD_DIRECTORY = settings.TENDERS_PATH_FRONT

from lib1 import title, pictures, upload

app.layout = html.Div(
    [
        pictures.DS4A_Img,
        pictures.Line_Img,
        title.title_backgroung,
        title.title_text,
        title.texto1,
        title.texto2,
        title.texto3,
        title.texto4,
        title.texto5,
        upload.upload
    ]
)


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    # Para guardar archivo en disco
    data = contents.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        print(UPLOAD_DIRECTORY)
        fp.write(base64.decodebytes(data))
        print('Guardado')
    fm.unzip_delete(UPLOAD_DIRECTORY,
                    file_name=filename)

    main_back.main()
    # print('Main se ejecutó')

    req_path = settings.DATA_FRAMES_PATH + "/" + settings.RESULTS_NAME

    df = pd.read_csv(req_path)

    plt.figure(figsize=(10, 10))

    fig = go.Figure(go.Bar(
        y=df["PATH"],
        x=(df["NUMBER"].astype(str)),
        orientation='h'))

    fig.update_layout(
        title={
            'text': "Páginas más probables",
            'y': 0.8,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        autosize=False,
        width=300,
        height=300,
        xaxis=dict(
            title_text="%Número de entidades",
            tickmode="array",
            titlefont=dict(size=15),
        ),
        yaxis=dict(
            title_text="Páginas y número de entidades",
            tickmode="array",
            titlefont=dict(size=15),
            tickformat=',d'
        ),
    )

    return dcc.Graph(figure=fig,
                     style={
                         'top': '50%',
                         'left': '50%'
                     })


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


#############################################################
if __name__ == "__main__":
    app.run_server(debug=True)
