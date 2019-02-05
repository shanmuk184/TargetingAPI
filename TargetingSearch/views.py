from django.template.loader import get_template
from django.http import HttpResponse
from django.template.response import TemplateResponse
import datetime
from facebookads.adobjects.targetingsearch import TargetingSearch
from .constants import get_location_params, get_interest_params
import simplejson as json
from django.shortcuts import render, redirect
from Targeting.serializers import LocationSerializer
from Targeting.models import LocationModel, InterestModel
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.template import Context


def index(request):

    return render(request, 'index.html',  {'locations': LocationModel.objects.all(), 'interests': InterestModel.objects.all()})


@csrf_exempt
def search_location(request):

    if(request.method == "POST"):
        new_data = request.POST['term']
        arr = new_data.split(' , ')
        new_location = LocationModel(
            key=arr[0], name=arr[1], region_id=arr[2], region=arr[3], country=arr[4], country_code=arr[5])
        new_location.save()

        return HttpResponse("success")

    params = get_location_params(request.GET['term'])
    resp = TargetingSearch.search(params=params)

    resp = list(map(lambda x: str(x["key"])+" , "+x["name"] +
                    " , "+str(x["region_id"])+" , "+x["region"]+" , "+x["country_name"]+" , "+str(x["country_code"]), list(resp)))
    return HttpResponse(json.dumps(resp))


@csrf_exempt
def search_interest(request):

    if(request.method == "POST"):
        new_data = request.POST['term']
        arr = new_data.split(' , ')
        new_location = InterestModel(
            id=arr[0], name=arr[1], path=arr[2], topic=arr[3], audience_size=arr[4], )
        new_location.save()

        return HttpResponse("success")
    params = get_interest_params(request.GET['term'])
    resp = TargetingSearch.search(params=params)
    resp = list(map(lambda x: str(x["id"])+" , "+x["name"] +
                    " , "+x["path"][0]+" , "+x["topic"]+' , '+str(x["audience_size"]), list(resp)))
    return HttpResponse(json.dumps(resp))
