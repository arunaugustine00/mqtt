import paho.mqtt.client as mqtt
import struct, random

client = mqtt.Client()
client.username_pw_set("iot", "1234")
client.connect("127.0.0.1", 1883, 60)

header = 'head'
footer = 'foot'

for i in range(0,10) :
	a = random.randint(0, 10) 
	b = random.randint(0, 100) 
	c = random.randint(100, 200)
	
	var = (header.encode('utf-8'),a,b,c,footer.encode('utf-8'))
	s = struct.Struct('4s iii 4s')
	packed_data = s.pack(*var) 
	
	client.publish("/feed1/random", packed_data)
	client.publish("/feed2/random", packed_data)
	client.loop()
