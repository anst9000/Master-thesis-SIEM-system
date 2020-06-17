#!/usr/bin/python3

import sys, json
import paho.mqtt.client as mqtt


def main(load):
#	print('load is', load)
	data = json.loads(load)
	broker_url = "mqtt.eclipse.org"
	broker_port = 1883

	client = mqtt.Client()
	client.connect(broker_url, broker_port)

	client.publish(
		topic="watcher/" + data['Topic'],
		payload=load,
		qos=1,
		retain=False)



if __name__ == "__main__":
	# Count the arguments
	arguments = len(sys.argv) - 1
	payload = sys.argv[1]
	main(payload)
