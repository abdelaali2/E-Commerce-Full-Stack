from django.apps import AppConfig
# from django.core.signals import request_finished


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
    
    def ready(self):
        from . import signals