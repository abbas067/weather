from django.shortcuts import render
import requests
import json
# Create your views here.
def page_count_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request,'testapp/count.html',{'count':newcount})
def index(request):
    url = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'
    city_weather = requests.get(url).json()
    print(city_weather)
    data=city_weather['wind']['speed']
    print("wind",data)
    d=city_weather['sys']['country']
    print(d)
    d1=city_weather['clouds']['all']
    print(d1)
    weather = {
        'city':city_weather['name'],
        'country':city_weather['sys']['country'],
        'icon':city_weather['weather'],
        'temperature' : city_weather['main']['temp']-273.15,
        'tempmin' : city_weather['main']['temp_min']-273.15,
        'tempmax' : city_weather['main']['temp_max']-273.15,
        'pressure' : city_weather['main']['pressure'],
         'wind':city_weather['wind']['speed'],
          'lon':city_weather['coord']['lon'],
        'lat':city_weather['coord']['lat'],
        'cloud':city_weather['clouds']['all'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    return render(request, 'testapp/index.html',{'weather':weather}) #returns the index.html template
