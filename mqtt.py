import paho.mqtt.client as mqtt #import the client1
import random

def publish( msg):
    broker_address= 'broker.mqttdashboard.com' #use external broker
    client = mqtt.Client(f'python-mqtt-{random.randint(0, 100)}') #create new instance
    client.connect(broker_address) #connect to broker
    print(f'Publishing: {msg}')
    client.publish("vitor/teste/canal1", msg)  # publish

