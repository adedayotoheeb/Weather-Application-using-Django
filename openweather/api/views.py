from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib import messages
from .forms import CityForm
from .models import City
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.
api_key = "7e9d94b50e9b5ea7df2bc5328167575d"

@csrf_exempt
def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=7e9d94b50e9b5ea7df2bc5328167575d&units=metric"

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            response = requests.get(url.format(new_city)).json()
            if response['cod'] == 200:
                form.save()
                messages.success(
                    request, f'{new_city} has been Successfully added ')
            else:
                messages.error(request, "City doesn't exist")

    form = CityForm()

    cities = City.objects.all()

    weather_data = []
    print('yaay')

    try:
        for city in cities:
            if str(city) == "None":
                city_weather = {
                    "city": None,
                    "temperature": None,
                    "description": None,
                    "icon": None,
                    "day": None,
                }
            else:
                response = requests.get(url.format(city)).json()
                city_weather = {
                    'city': city.name,
                    'temperature': response['main']['temp'],
                    'description': response['weather'][0]['description'],
                    'icon': response['weather'][0]['icon'],
                    'day':  datetime.date.today()
                }
            weather_data.append(city_weather)
    except Exception as e:
        print(e)


    context = {'weather_data': weather_data, "form": form}
    return render(request, 'api/index.html', context)
