import time
import signal
import board
import adafruit_ads1x15.ads1015 as ADS

from celery import shared_task

from rpi import Relay, Reservoir, Sensor
from .event_handler import EventHandler

lamp_relay = Relay(board.D12)
pump_relay = Relay(board.D16)

warm_sensor = Sensor(board.D18)
cool_sensor = Sensor(board.D23)
hide_sensor = Sensor(board.D24)

pump_reservoir = Reservoir(board.SCL, board.SDA, ADS.P0)

event_handler = EventHandler()

@shared_task
def take_reading():
    now = int(time.time())
    event_handler.submit(
        type='warm-sensor',
        timestamp=now,
        payload=warm_sensor.read()
    )
    event_handler.submit(
        type='cool_sensor',
        timestamp=now,
        payload=cool_sensor.read()
    )
    event_handler.submit(
        type='hide_sensor',
        timestamp=now,
        payload=hide_sensor.read()
    )
    event_handler.submit(
        type='water_level',
        timestamp=now,
        payload=pump_reservoir.level()
    )

@shared_task
def mist_burst(duration):
    signal.signal(signal.SIGINT, pump_relay.exit)

    pump_on.apply_async()
    pump_off.apply_async(countdown=duration)


@shared_task
def pump_on():
    pump_relay.on()
    event_handler.submit(
        type='pump',
        timestamp=int(time.time()),
        payload={'on': True}
    )

@shared_task
def pump_off():
    pump_relay.off()
    event_handler.submit(
        type='pump',
        timestamp=int(time.time()),
        payload={'on': False}
    )

@shared_task
def lamp_on():
    lamp_relay.on()
    event_handler.submit(
        type='light',
        timestamp=int(time.time()),
        payload={'on': True}
    )

@shared_task
def lamp_off():
    lamp_relay.off()
    event_handler.submit(
        type='light',
        timestamp=int(time.time()),
        payload={'on': False}
    )
