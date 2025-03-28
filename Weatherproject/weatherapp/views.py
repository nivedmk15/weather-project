from django.shortcuts import render
import requests
import datetime

def home(req):
    city = 'kannur'
    if req.POST:
        city = req.POST['city']
        
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1751f8eea7b6348525f077ba5866d206"
    
    PARAMS = {
        'units' : 'metric'
    }
    
    data = requests.get(url,PARAMS).json()
    
    date = datetime.datetime.today()
    
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    
    
    
    return render(req,'weather.html')
