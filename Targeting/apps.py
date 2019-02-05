from django.apps import AppConfig
from facebookads.api import FacebookAdsApi
from django.conf import settings


class TargetingConfig(AppConfig):
    name = 'Targeting'
    # Initialize a new Session and instantiate an API object:
    FacebookAdsApi.init(settings.ACCESS_TOKEN)
