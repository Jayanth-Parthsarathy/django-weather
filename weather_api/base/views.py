from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
from . import config
api_key = config.API_KEY


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city, api_key)).json()
    context = {'weather': city_weather}
    return render(request, 'base/index.html', context=context)
