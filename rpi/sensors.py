import time

from .setup import dht, level_sensor
from celery import shared_task

@shared_task
def read():
    return {
        'timestamp': int(time.time()),
        'warm': read_dht_sensor(dht['warm_end']),
        'cool': read_dht_sensor(dht['cool_end']),
        'hide': read_dht_sensor(dht['hide_box']),
        'water': read_reservoir_level(level_sensor),
    }


def read_reservoir_level(sensor):
    result = sensor['input']
    percent_full = (sensor['min_ohm']-result.value)/(sensor['min_ohm']-sensor['max_ohm'])
    return {
        'percent': round(percent_full*100, 2),
        'depth': round(percent_full*sensor['length_cm'], 1)
    }

def read_dht_sensor(dht):
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        return {
            'temperature': temperature,
            'humidity': humidity,
        } 
    except RuntimeError as e:
        return {
            'error': e.args
        }
