from django.apps import AppConfig

class BboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bboard'

    def ready(self):
        from bboard.templatetags import custom_tags