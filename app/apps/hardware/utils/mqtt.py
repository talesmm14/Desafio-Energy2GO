from typing import Callable

from paho.mqtt import client as mqtt_client

from config.settings import MQTT_PASSWORD, CLIENT_ID, MQTT_USERNAME, MQTT_ADDRESS, MQTT_PORT


def send_message(topic: str, message: str) -> None:
    """ Envia uma mensagem para um tópico via MQTT. """
    client = mqtt_client.Client(callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.connect(MQTT_ADDRESS, MQTT_PORT)
    client.loop_start()
    client.publish(topic, message)
    client.loop_stop()
    client.disconnect()


def subscribe_topic(topic: str, on_message: Callable) -> None:
    """ Se inscreve em um tópico e escuta uma mensagem para processar com a função enviada. """
    client = mqtt_client.Client(callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.connect(MQTT_ADDRESS, MQTT_PORT)
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()
