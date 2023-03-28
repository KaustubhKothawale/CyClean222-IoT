# Description: This file contains the class Bulb which is used to represent a bulb in the system.
class Bulb:
    def __init__(self):
        self.state = 'off'
        self.brightness = 0

    def on(self):
        self.state = 'on'

    def off(self):
        self.state = 'off'

    def set_brightness(self, brightness):
        self.brightness = brightness

    def get_state(self):
        return self.state

    def get_brightness(self):
        return self.brightness