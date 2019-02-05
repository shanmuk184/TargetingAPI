from django.conf import settings
from facebookads.adobjects.targetingsearch import TargetingSearch
from TargetingSearch.constants import get_location_params

params = {
    'q': "cricket",
    'type': 'adinterest',
    'access_token': settings.ACCESS_TOKEN
}


def run():
    resp = TargetingSearch.search(params)
    print(resp)
