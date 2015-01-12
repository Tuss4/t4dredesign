FROM ubuntu:trusty
MAINTAINER tuss4 <tuss4dbfn@gmail.com>
RUN mkdir /code || true
WORKDIR /code
ADD requirements.txt /code/

RUN apt-get update -qq && \
    apt-get install -y -qq socat git python-psycopg2 libpq-dev \
    python2.7-dev gunicorn g++ make python-dev wget

RUN wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
RUN python get-pip.py

RUN pip install -U fig

RUN pip install -r requirements.txt

ADD . /code/

WORKDIR /code/t4dredesign

EXPOSE 8080
