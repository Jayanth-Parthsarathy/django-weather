from .forms import CityForm
from .models import City
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
from . import config
api_key = config.API_KEY


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    weather_data = []
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    for city in cities:
        city_weather = requests.get(url.format(city, api_key)).json()
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'base/index.html', context=context)
