FROM python:slim

RUN pip install Nikola[extras]

RUN apt-get update && apt-get install -y git

RUN mkdir /biblioln.es
RUN mkdir $HOME/.ssh
WORKDIR /biblioln.es
