#!/usr/bin/env/ python 3        
import paho.mqtt.client as mqtt

brokerIP        = "192.168.1.64"
brokerPort      = 1883
brokerKeepAlive = 60
myTopic         = "plant1/temp"

def on_connect (client, userdata, flags, rc):
        print ("Connected with code" + str(rc))
        client.subscribe(myTopic)

def message (client, userdata, msg):
        print("fetched:" + str(msg.payload.decode())+"from topic" + Mytopic)
        client.disconnect()

client = mqtt.client()
client.connect(brokerIP, brokerPort, brokerKeepAlive)
client.on_connect = on_connect
client.on_message = message
client.loop_forever()
