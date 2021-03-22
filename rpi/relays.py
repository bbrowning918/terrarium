import time

import digitalio

from .setup import light, pump
from celery import shared_task, chain

@shared_task
def light_on():
    relay_on(light)
    return {
        'timestamp': int(time.time()),
        'light': True
    }

@shared_task
def light_off():
    relay_off(light)
    return {
        'timestamp': int(time.time()),
        'light': False
    }

@shared_task
def pump_run_10_sec():
    pump_on.apply_async()
    pump_off.apply_async(countdown=10)

@shared_task
def pump_on():
    pump.value = False
    # relay_on(pump)
    return {
        'timestamp': int(time.time()),
        'pump': True
    }

@shared_task
def pump_off():
    pump.value = True
    # relay_off(pump)
    return {
        'timestamp': int(time.time()),
        'pump': False
    }

def relay_on(relay):
    relay.value = True

def relay_off(relay):
    relay.value = False
