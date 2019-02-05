from django.db import models
from .apps import TargetingConfig

# Create your models here.


class LocationModel(models.Model):
    dbid = models.AutoField(primary_key=True)
    key = models.CharField(max_length=50)
    name = models.CharField(blank=True, null=True, max_length=50)
    region_id = models.CharField(blank=True, null=True, max_length=50)
    region = models.CharField(blank=True, null=True, max_length=50)
    country = models.CharField(blank=True, null=True, max_length=50)
    country_code = models.CharField(blank=True, null=True, max_length=100)

    class Meta:
        db_table = TargetingConfig.name+"_location"


class InterestModel(models.Model):
    dbid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=50)
    name = models.CharField(blank=True, null=True, max_length=50)
    path = models.CharField(blank=True, null=True, max_length=50)
    topic = models.CharField(blank=True, null=True, max_length=50)
    audience_size = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = TargetingConfig.name+"_interest"
