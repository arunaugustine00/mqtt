# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import struct 

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/feed2/random")

def on_message(client, userdata, msg):
    var = struct.unpack('iii',msg.payload) 
    a, b, c = var[0], var[1], var[2]
    print("a = {}, b = {}, c = {}".format(a,b,c))
  
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("iot", "1234")
client.connect("127.0.0.1", 1883, 60)
client.loop_forever()
