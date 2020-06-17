import paho.mqtt.client as mqtt
from store_to_db import sensor_Data_Handler

# MQTT Settings
MQTT_Broker = "192.168.0.31"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "Home/BedRoom/#"


# Subscribe to all Sensors at Base Topic
def on_connect(mosq, obj, rc):
    print('connecting...')


# Save Data into DB Table
def on_message(mosq, obj, msg):
    print('-------------------')
    # This is the Master Call for saving MQTT Data into DB
    # For details of "sensor_Data_Handler" function please refer "sensor_data_to_db.py"
    print("MQTT Data Received...")
    print("MQTT Topic: " + msg.topic)
    print("Data: ")
    print(msg.payload)
    sensor_Data_Handler(msg.topic, msg.payload)


def on_subscribe(mosq, obj, mid, granted_qos):
    print("MQTT Subscribing...")


mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
mqttc.subscribe(MQTT_Topic, qos=1)

# Continue the network loop
mqttc.loop_forever()
