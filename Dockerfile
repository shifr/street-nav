FROM python:3.7

ADD . /service
WORKDIR /service

RUN python setup.py install
