import paho.mqtt.client as mqtt
import struct, random

client = mqtt.Client()
client.username_pw_set("iot", "1234")
client.connect("127.0.0.1", 1883, 60)

for i in range(0,10) :
	a = random.randint(0, 10) 
	b = random.randint(0, 100) 
	c = random.randint(100, 200) 
	var = struct.pack('iii',a,b,c)
	client.publish("/feed1/random", var)
	client.publish("/feed2/random", var)
	client.loop()
