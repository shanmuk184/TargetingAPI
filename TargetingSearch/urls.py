"""TargetingSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index, search_location, search_interest
from django.conf.urls import url, include
from facebookads.api import FacebookAdsApi
from django.conf import settings
from rest_framework import routers
FacebookAdsApi.init(settings.ACCESS_TOKEN)
router = routers.SimpleRouter()
# router.register(,  base_name='location')
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', index),
    url(r'^search-location/$', search_location),
    url(r'^search-interest/$', search_interest),
]
