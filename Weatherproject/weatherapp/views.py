from django.shortcuts import render
import requests
import datetime

def home(req):
    city = 'kochi'
    if req.POST:
        city = req.POST['city']
    
    date = datetime.datetime.today()
    
    
    PARAMS = {
        'units' : 'metric'
    }
    
    try:
        # created url with city name and api
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1751f8eea7b6348525f077ba5866d206"
        data = requests.get(url,PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        error_occured = False
    except:
        
        url = f"https://api.openweathermap.org/data/2.5/weather?q=kochi&appid=1751f8eea7b6348525f077ba5866d206"
        data = requests.get(url,PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        city = 'kochi'
        error_occured = True
        
        
    context = {
        'city':city,
        'description':description,
        'icon':icon,
        'temp':temp,
        'date':date,
        'error_occured' : error_occured
    }
    
    
    return render(req,'weather.html',context)
