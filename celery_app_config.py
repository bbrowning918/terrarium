from celery.schedules import crontab, solar

broker_url = 'redis://localhost:6379/0'

imports = ('tasks',)

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
    'mist_bursts': {
        'task': 'tasks.mist_burst',
        'schedule': crontab(minute=0, hour='6-21'),
        'kwargs': {'duration': 15}
    }
}
