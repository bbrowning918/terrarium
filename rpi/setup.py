import board
import adafruit_dht
import busio
import digitalio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

dht = {
    'warm_end': adafruit_dht.DHT22(board.D18, use_pulseio=False),
    'cool_end': adafruit_dht.DHT22(board.D23, use_pulseio=False),
    'hide_box': adafruit_dht.DHT22(board.D24, use_pulseio=False),
}

level_sensor = {
    'input': AnalogIn(ADS.ADS1015(busio.I2C(board.SCL, board.SDA)), ADS.P0),
    'max_ohm': 24300,
    'min_ohm': 19300,
    'length_cm': 30,
}

light = digitalio.DigitalInOut(board.D12)
light.direction = digitalio.Direction.OUTPUT

pump = digitalio.DigitalInOut(board.D20)
# pump = digitalio.DigitalInOut(board.D16)
pump.direction = digitalio.Direction.OUTPUT
# pump.switch_to_output(value=True)

# relay3 = digitalio.DigitalInOut(board.D20)
# relay3.direction = digitalio.Direction.OUTPUT

# relay4 = digitalio.DigitalInOut(board.D21)
# relay4.direction = digitalio.Direction.OUTPUT
