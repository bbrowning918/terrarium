from celery import Celery

celery_app = Celery('terrarium')

celery_app.config_from_object('celery_app_config')
