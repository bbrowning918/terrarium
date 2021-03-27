from celery.schedules import crontab, solar

broker_url = 'redis://localhost:6379/0'

imports = ('tasks',)

result_backend ='redis://localhost:6379/1'
result_expires = 604800

beat_schedule = {
    # 'sensors_read': {
    #     'task': 'rpi.sensors.read',
    #     'schedule': crontab(minute='*/15'),
    # },
    # 'light_on': {
    #     'task': 'rpi.relays.light_on',
    #     'schedule': solar('dawn_civil', -15.9, -46.0),
    # },
    # 'light_off': {
    #     'task': 'rpi.relays.light_off',
    #     'schedule': solar('dusk_civil', -15.9, -46.0),
    # },
    'pump_10s_pulse': {
        'task': 'tasks.run_10_sec',
        'schedule': crontab(),
    }
    # 'pump_on': {
    #     'task': 'rpi.relays.pump_on',
    #     'schedule': crontab(minute='0-58/2'),
    # },
    # 'pump_off': {
    #     'task': 'rpi.relays.pump_off',
    #     'schedule': crontab(minute='1-59/2'),
    # },
}
