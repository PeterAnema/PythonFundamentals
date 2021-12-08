import urllib.request
import json

city = 'amsterdam'

url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=d1526a9039658a6f76950cff21823aff&units=metric' % city

with urllib.request.urlopen(url) as f:
    data = json.load(f)

    temperature = data['main']['temp']

    print('The temperature in %s is %f' % (city, temperature))