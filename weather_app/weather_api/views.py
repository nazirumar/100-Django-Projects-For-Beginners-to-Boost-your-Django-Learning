from django.shortcuts import render
from weather_api.api import respon_api
# Create your views here.


def index(request):
    print(respon_api().Daily())
    context ={
        'longtitude':round(respon_api().Longitude()),
        'latitude': round(respon_api().Longitude()),

    }
    return render(request, 'index.html', context)
