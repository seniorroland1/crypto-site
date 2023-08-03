from django.apps import AppConfig


class DashbaordConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashbaord'


    def ready(self):
        from dashbaord.updater import start
        start()