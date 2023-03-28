# CyClean222-IoT
To run this please install mosquitto broker on your local machine.

sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients

Set the username to "username" and password to "pass"

Description:
1. Device 
  Please run device.py file to control the bulb, subscribe to topics and publish data back to the MQTT broker.
2. Bulb Remote:
  As an additional functionality we can control the bulb from a remote. This can be done by runing bulb_remote.py. We can change the brightness and state of the bulb by changing the values in file bulb_brightness and bulb_state respictely.
