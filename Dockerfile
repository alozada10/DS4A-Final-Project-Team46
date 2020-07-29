FROM continuumio/miniconda3

# files
COPY app_data app_data
COPY jobs jobs
COPY myappdirectory_elias myappdirectory_elias
COPY utils utils
COPY requirements.txt /tmp/

# workdir
WORKDIR myappdirectory_elias/myappdirectory/app

# dependences
RUN apt-get install -y apt-utils
RUN apt-get install -y tesseract-ocr
RUN apt-get install -y tesseract-ocr-spa
RUN apt-get install -y imagemagick
RUN conda install --file /tmp/requirements.txt

# port
EXPOSE 8050

# execute entrypoint
CMD ["python", dashboard.py]