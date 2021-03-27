import time
import signal
import board
import adafruit_ads1x15.ads1015 as ADS

from celery import shared_task, chain

from rpi.relay import Relay
from rpi.sensor import Sensor
from rpi.reservoir import Reservoir

lamp_relay = Relay(board.D12)
pump_relay = Relay(board.D16)

warm_sensor = Sensor(board.D18)
cool_sensor = Sensor(board.D23)
hide_sensor = Sensor(board.D24)

reservoir = Reservoir(board.SCL, board.SDA, ADS.P0)

# unused
# 3_relay = Relay(board.D20)
# 4_relay = Relay(board.D21)

@shared_task
def run_10_sec():
    signal.signal(signal.SIGINT, lamp_relay.exit)

    lamp_on.apply_async()
    lamp_off.apply_async(countdown=10)

    return {
        'timestamp': int(time.time()),
        'warm': warm_sensor.read(),
        'cool': cool_sensor.read(),
        'hide': hide_sensor.read(),
        'water': reservoir.level(),
    }

@shared_task
def lamp_on():
    lamp_relay.on()
    return {
        'timestamp': int(time.time()),
        'light': True
    }

@shared_task
def lamp_off():
    lamp_relay.off()
    return {
        'timestamp': int(time.time()),
        'light': False
    }
