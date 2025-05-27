from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class AboutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'

class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'