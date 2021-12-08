import requests

city = 'new york'

url  = 'http://api.openweathermap.org/data/2.5/weather'\
       '?q=%s'\
       '&appid=d1526a9039658a6f76950cff21823aff'\
       '&lang=en'\
       '&units=metric' % city

r = requests.get(url)

data = r.json()
print(data)

temperature = data['main']['temp']
feels_like = data['main']['feels_like']
description = data['weather'][0]['description']

print('In %s it is now %d°C with %s but it feels like %d°C' % (city.capitalize(),
                                                               temperature,
                                                               description,
                                                               feels_like))