FROM ubuntu
LABEL authors="talesmelquiades : talesmelquiades@hotmail.com"

RUN apt-get update
RUN apt install -y build-essential
RUN apt install -y gcc
RUN apt install -y make
RUN apt install -y libssl-dev

WORKDIR /app

COPY . .

RUN cd libs/paho.mqtt.c && make && make install

RUN gcc main.c -o equipamento -lpaho-mqtt3c -Wall

CMD ["./equipamento"]