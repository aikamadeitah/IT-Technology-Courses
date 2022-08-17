#! /usr/bin/env python3
import paho.mqtt.client as mqtt
import random

brokerIP = "192.168.1.64"
brokerPort = 1883
brokerKeepAlive = 60

myTopic = "plant1/temp"
myPayload = random.randint(1,101)
myQoS = 1
myRetain = True 

client = mqtt.Client()
client.connect(brokerIP, brokerPort, BrokerKeepAlive)
client.publish(topic =	myTopic, qos = myQoS, payload = myPayload, retain = myretain)
print(srt(myPayload)+"is beeing published on broker " + brokerIP +" : "+ str(brokerPort) + " on topic" + myTopic )
client.disconnect() 