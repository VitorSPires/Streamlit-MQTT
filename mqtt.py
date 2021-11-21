import paho.mqtt.client as mqtt #import the client1
import random

def setup():
    print('setting up')
    broker_address= 'broker.mqttdashboard.com' #use external broker
    client = mqtt.Client(f'python-mqtt-{random.randint(0, 10000)}') #create new instance
    client.connect(broker_address) #connect to broker
    #client.publish("vitor/teste/canal1", msg)  # publish
    return(client)


