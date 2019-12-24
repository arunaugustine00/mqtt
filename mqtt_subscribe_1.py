import paho.mqtt.client as mqtt
import struct 

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))
	client.subscribe("/feed1/random")

def on_message(client, userdata, msg):
	packed_data = msg.payload 
	s = struct.Struct('4s iii 4s')
	unpacked_data = s.unpack(packed_data) 

	if unpacked_data[0] == b'head' and unpacked_data[4] == b'foot' : 
		a, b, c = unpacked_data[1], unpacked_data[2], unpacked_data[3]
		print("a = {}, b = {}, c = {}".format(a,b,c))
	else:
		print('packet corrupted')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("iot", "1234")
client.connect("127.0.0.1", 1883, 60)
client.loop_forever()
