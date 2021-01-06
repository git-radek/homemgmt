import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):  
    print("Connected with result code {0}".format(str(rc)))  
    client.subscribe("stat/taras1/POWER")


def on_message(client, userdata, msg): 
    print("Message received-> " + msg.topic + " " + str(msg.payload)) 


client = mqtt.Client("taras1")
client.on_connect = on_connect
client.on_message = on_message
client.connect('127.0.0.1', 1883, 60)
client.loop_forever()  # Start networking daemon
