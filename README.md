# MQTT

MQTT is a Protocol used for IOT projects.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install paho-mqtt.

```bash
sudo apt-get update
sudo apt-get install mosquitto
pip install paho-mqtt
```

## Usage

```python
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.username_pw_set("username", "password")
client.connect("127.0.0.1", 1883, 60)

client.publish("/feed", "Hello")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
