import paho.mqtt.client as mqttClient
import bulb
import time

# Creating the bulb object
bulb = bulb.Bulb()

# On connecting to the broker


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed")

# On receiving a message from the broker


def on_message(mosq, obj, msg):
    # Taking the action based on the topic and payload
    # Changing the state
    if msg.topic == 'smart-light-bulb/state':
        # print("inside state")
        if(msg.payload.decode() == "on"):
            print("bulb set on")
            bulb.on()
            #
        elif(msg.payload.decode() == 'off'):
            print("bulb set off")
            bulb.off()
    # changing the brightness
    if msg.topic == 'smart-light-bulb/brightness':
        print("setting brightness to", msg.payload.decode(), "")
        bulb.set_brightness(msg.payload.decode())
    # publishing the acknowledgement
    mosq.publish('pong', 'ack', 0)


if __name__ == '__main__':
    # Setting initial state of bulb
    bulb.on()
    bulb.set_brightness(100)
    # Creating the client
    client = mqttClient.Client()
    broker_address = "localhost"  # Broker address
    port = 1883  # Broker port
    user = "username"  # Connection username
    password = "pass"  # Connection password

    client.username_pw_set(user, password=password)
    client.on_message = on_message
    client.on_connect = on_connect

    client.connect(broker_address, port, 60)
    # subscribing to the topics
    client.subscribe("smart-light-bulb/state", 0)
    client.subscribe("smart-light-bulb/brightness", 0)
    # starting the loop
    client.loop_start()

try:
    # publishing the state and brightness of the bulb
    while True:
        client.publish("smart-light-bulb/state", bulb.get_state())
        client.publish("smart-light-bulb/brightness", bulb.get_brightness())
        print("Current State and brightness at time:", time.time(),
              "is", bulb.get_state(), bulb.get_brightness())
        time.sleep(1)
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
except Exception as e:
    print(e)
    client.disconnect()
    client.loop_stop()
