#!/usr/bin/env python3

import paho.mqtt.client as mqtt

broker_url = "mqtt.eclipse.org"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " (rc))


def on_message_from_mosquitto(client, userdata, message):
    print("Message Recieved from Mosquitto: " + message.payload.decode())


def on_message_from_syslog(client, userdata, message):
    print("Message Recieved from syslog: "+message.payload.decode())


def on_message_from_postgres(client, userdata, message):
    print("Message Recieved from PostgreSQL: "+message.payload.decode())


def on_message(client, userdata, message):
    print("Message Recieved: "+message.payload.decode())


client = mqtt.Client()
client.on_connect = on_connect

# To Process Every Other Message
#client.on_message = on_message
client.connect(broker_url, broker_port)

client.subscribe("watcher/Mosquitto", qos=1)
client.subscribe("watcher/syslog", qos=1)
client.subscribe("watcher/PostgreSQL", qos=1)

client.message_callback_add("watcher/Mosquitto", on_message_from_mosquitto)
client.message_callback_add("watcher/syslog", on_message_from_syslog)
client.message_callback_add("watcher/PostgreSQL", on_message_from_postgres)

client.loop_forever()
