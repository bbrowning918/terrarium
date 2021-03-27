import board
import digitalio 


class Relay:
    _relay = None

    # wired as NO, relay closes when driven low/false
    ON = False
    OFF = True

    def __init__(self, pin):
        self._relay = digitalio.DigitalInOut(pin)
        self._relay.switch_to_output(value=self.OFF)

    def on(self):
        self._relay.value = self.ON

    def off(self):
        self._relay.value = self.OFF

    def exit(self, sigterm, frame):
        self._relay.value = self.OFF
        self._relay.deinit()
