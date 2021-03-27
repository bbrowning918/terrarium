import board
import adafruit_dht


class Sensor:
    _sensor = None

    def __init__(self, pin):
        self._sensor = adafruit_dht.DHT22(pin, use_pulseio=False)

    def read(self):
        try:
            temperature = self._sensor.temperature
            humidity = self._sensor.humidity
            return {
                'temperature': temperature,
                'humidity': humidity,
            } 
        except RuntimeError as e:
            return {
                'error': e.args
            }
