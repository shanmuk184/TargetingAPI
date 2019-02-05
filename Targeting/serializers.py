from rest_framework import serializers
from .models import LocationModel


class LocationSerializer(serializers.Serializer):
    class Meta:
        model = LocationModel
        fields = ("key", "name", "region_id",
                  "region", "country", "country_code")
