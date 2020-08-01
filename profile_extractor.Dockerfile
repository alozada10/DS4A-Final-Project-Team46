#FROM continuumio/miniconda3
#FROM python:3.6
FROM gcr.io/google-appengine/python

RUN apt-get update -y
RUN apt-get install poppler-utils -y
RUN virtualenv -p python3.7 /env

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ENV PYTHONPATH /:$PYTHONPATH

# dependences
#RUN apt-get update -y
#RUN apt-get install apt-utils -y
#RUN apt-get install -y tesseract-ocr
#RUN apt-get install -y tesseract-ocr-spa
#RUN apt-get install -y imagemagick
#RUN apt-get install poppler-utils -y
RUN pip install --upgrade pip


# files
COPY app_data app_data
COPY jobs jobs
COPY myappdirectory_elias myappdirectory_elias
COPY utils utils
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# workdir
WORKDIR myappdirectory_elias/myappdirectory/app



# port
EXPOSE 8050



#ENV VIRTUAL_ENV /env
#ENV PATH /env/bin:$PATH

CMD [python, dashboard.py]

