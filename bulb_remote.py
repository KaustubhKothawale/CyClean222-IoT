import paho.mqtt.client as mqttClient
import time

# connecting to the broker


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed")


broker_address = "localhost"
port = 1883
user = "username"
password = "pass"

client = mqttClient.Client()  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.connect(broker_address, port=port, keepalive=60)  # connect to broker

# Error handling
try:
    while True:
        # redding the state and brightness from the file
        f_state = open('./bulb_state.txt', 'r')
        f_brightnesss = open('./bulb_brightness.txt', 'r')
        state = f_state.read()
        brightness = f_brightnesss.read()

        # publishing the state and brightness to the broker
        print(state, brightness)
        client.publish("smart-light-bulb/state", state)
        client.publish("smart-light-bulb/brightness", brightness)
        # closing the files
        f_state.close()
        f_brightnesss.close()
        time.sleep(1)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
except Exception as e:
    print(e)
    client.disconnect()
    client.loop_stop()
