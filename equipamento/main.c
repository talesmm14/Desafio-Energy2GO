#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <regex.h>
#include <time.h>
#include <MQTTClient.h>
#define MQTT_ADDRESS getenv("MQTT_ADDRESS")
#define CLIENTID "MQTTCClientID"
#define EQUIPMENT_VALIDATION_TOPIC "EQUIPMENT/VALIDATION"
#define EQUIPMENT_VALIDATION_RESPONSE_TOPIC "EQUIPMENT/VALIDATION/RESPONSE"
#define MQTT_USERNAME getenv("MQTT_USERNAME")
#define MQTT_PASSWORD getenv("MQTT_PASSWORD")

MQTTClient client;

void publish(MQTTClient client, char *topic, char *payload);

int on_message(void *context, char *topicName, int topicLen, MQTTClient_message *message);

void publish(MQTTClient client, char *topic, char *payload) {
    MQTTClient_message pubmsg = MQTTClient_message_initializer;

    pubmsg.payload = payload;
    pubmsg.payloadlen = strlen(pubmsg.payload);
    pubmsg.qos = 2;
    pubmsg.retained = 0;
    MQTTClient_deliveryToken token;
    MQTTClient_publishMessage(client, topic, &pubmsg, &token);
    MQTTClient_waitForCompletion(client, token, 1000L);
}

int on_message(void *context, char *topicName, int topicLen, MQTTClient_message *message) {
    char *payload = message->payload;
    int id;
    char response[100];
    if (sscanf(payload, "transaction {%d}", &id) == 1) {
        srand(time(NULL));
        if (((rand() % (10 - 1 + 1)) + 1) >= 5){
            sprintf(response, "confirm transaction {%d}\n", id);
        } else {
            sprintf(response, "error transaction {%d}\n", id);
        }
        printf("%s", response);
        publish(client, EQUIPMENT_VALIDATION_RESPONSE_TOPIC, response);
        MQTTClient_freeMessage(&message);
        MQTTClient_free(topicName);
        return 1;
    }
    fputs("Erro: não foi possível analisar a transação.\n", stderr);
    return 1;
}

int main(int argc, char *argv[]) {
    int rc;
    MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
    conn_opts.username = MQTT_USERNAME;
    conn_opts.password = MQTT_PASSWORD;
    MQTTClient_create(&client, MQTT_ADDRESS, CLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL);
    MQTTClient_setCallbacks(client, NULL, NULL, on_message, NULL);

    rc = MQTTClient_connect(client, &conn_opts);

    if (rc != MQTTCLIENT_SUCCESS) {
        printf("\n\rFalha na conexao ao broker MQTT. Erro: %d\n", rc);
        exit(-1);
    }

    MQTTClient_subscribe(client, EQUIPMENT_VALIDATION_TOPIC, 0);
    while (1) {
    }
}