from celery.schedules import crontab, solar

broker_url = 'redis://localhost:6379/0'

imports = ('tasks',)

result_backend ='redis://localhost:6379/1'
result_expires = 604800

timezone = 'Canada/Saskatchewan'

beat_schedule = {
    'sensors_read': {
        'task': 'tasks.take_reading',
        'schedule': crontab(minute='*/15'),
    },
    'light_on': {
        'task': 'tasks.lamp_on',
        'schedule': solar('dawn_civil', 52.1, -106.6),
    },
    'light_off': {
        'task': 'tasks.lamp_off',
        'schedule': solar('dusk_civil', 52.1, -106.6),
    },
    'mist_10s': {
        'task': 'tasks.mist_10_sec',
        'schedule': crontab(minute=5, hour='6,9,12,15,18,21'),
    }
}
