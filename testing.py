import digitalio
import board
import busio
import adafruit_dht
from time import sleep

import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0)

dht1 = adafruit_dht.DHT22(board.D18)
dht2 = adafruit_dht.DHT22(board.D23)
dht3 = adafruit_dht.DHT22(board.D24)

# relay1 = digitalio.DigitalInOut(board.D12)
# relay1.direction = digitalio.Direction.OUTPUT

# relay2 = digitalio.DigitalInOut(board.D16)
# relay2.direction = digitalio.Direction.OUTPUT

# relay3 = digitalio.DigitalInOut(board.D20)
# relay3.direction = digitalio.Direction.OUTPUT

# relay4 = digitalio.DigitalInOut(board.D21)
# relay4.direction = digitalio.Direction.OUTPUT

SENSOR_MAX = 24300
SENSOR_MIN = 19300
SENSOR_LENGTH = 30 # cm

DELAY = 3

def read_dht(dht):
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        # Print what we got to the REPL
        print("Temp: {:.1f} *C \t Humidity: {}%".format(temperature, humidity))
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)

while True:
    # relay1.value = True
    # sleep(DELAY)
    # relay1.value = False
    # sleep(DELAY)
    # relay2.value = True
    # sleep(DELAY)
    # relay2.value = False
    # sleep(DELAY)
    percent_full = (SENSOR_MIN-chan.value)/(SENSOR_MIN-SENSOR_MAX)

    print(f'{round(percent_full*100, 1)}%, {round(percent_full*SENSOR_LENGTH, 1)} cm')
    sleep(DELAY)

    read_dht(dht1)
    sleep(DELAY)
    read_dht(dht2)
    sleep(DELAY)
    read_dht(dht3)
    sleep(DELAY)
