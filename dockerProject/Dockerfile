FROM ubuntu:16.04

RUN apt-get update -y 

RUN apt-get install -y python-pip python-dev

WORKDIR /app

RUN apt-get install python-flask -y

COPY ./api /app

ENTRYPOINT [ "python" ]

CMD [ "api.py" ]