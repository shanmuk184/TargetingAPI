from django.conf import settings


def get_location_params(data):
    return {
        'q': data,
        'type': 'adgeolocation',
        'location_types': ['country', 'city'],
        'access_token': settings.ACCESS_TOKEN,
    }


def get_interest_params(data):
    return {
        'q': data,
        'type': 'adinterest',
        'access_token': settings.ACCESS_TOKEN,

    }
