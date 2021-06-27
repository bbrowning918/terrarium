import busio
import adafruit_ads1x15.ads1015 as ads
from adafruit_ads1x15.analog_in import AnalogIn


class Reservoir:
    _level_sensor = None

    MAX_OHM = 24300
    MIN_OHM = 19300
    LENGTH_CM = 30

    def __init__(self, scl, sda, input_pin):
        ads1015 = ads.ADS1015(busio.I2C(scl, sda))
        self._level_sensor = AnalogIn(ads1015, input_pin)

    def level(self):
        result = self._level_sensor
        percent_full = (self.MIN_OHM-result.value)/(self.MIN_OHM-self.MAX_OHM)
        return {
            'percent': round(percent_full*100, 2),
            'depth': round(percent_full*self.LENGTH_CM, 1)
        }
