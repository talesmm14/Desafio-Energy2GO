#!/bin/bash

mosquitto_pub -h mosquitto -t baterias_livres -m "0"

mosquitto_pub -h mosquitto -t transacao -m "Iniciando transações"
