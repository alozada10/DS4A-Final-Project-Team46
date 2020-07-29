# Descarga la imagen miniconda3 del repositorio continuumio 
# de la página de Docker

FROM continuumio/miniconda3

################################################

# Instala en linux las dependencias apt-utils 
# (para poder instalar otras dependencias de linux), 
# tesseract-ocr, tesseract-ocr-spa
# (para instalar tesseract y su paquete de OCR en Español),
# e imagemagick (para apoyar a tesseract en su labor)

RUN apt-get install -y apt-utils
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y tesseract-ocr-spa
RUN apt-get install -y imagemagick

################################################

# Copia el archivo de requerimientos de las librerías al 
# folder de archivos temporales y el folder de la aplicación 
# a la carpeta "app. Acto seguido, cambia de directorio activo
# a "app".

COPY requirements.txt /tmp/
COPY ./app /app
WORKDIR "/app"

#################################################

# Instala las librerías requeridas de Pychon con Conda

RUN conda install --file /tmp/requirements.txt

#################################################

# Expone al exterior el puerto 8050 en el contenedor
# (de ahí que la URL siempre tenga el número 8050
# como sufijo).

EXPOSE 8050

#################################################

# "ENTRYPOINT" es una manera más fuerte de ejecutar un comando en linux bash,
# adecuada para cuando se desea que la imagen sólo ejecute una sola cosa 
# (el dashboard, en nuestro caso). Así las cosas, se inicia Python y
# se ejecuta dashboard.py desde el inicio, inicializando así el dashboard.

ENTRYPOINT [ "python3" ]
CMD [ "dashboard.py" ]