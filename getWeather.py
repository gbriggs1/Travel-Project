import requests

#NOTE: This function returns a list with 3 elements: temperature in Farenheit, temperature description (cloudy/clear/rain), link to image of temperature description.
def getWeather(lat, lon):
    l = []
    response = requests.get("https://fcc-weather-api.glitch.me/api/current?lat="+str(lat)+"&lon="+str(lon))
    # response = requests.get("https://fcc-weather-api.glitch.me/api/current?lat=39.9526&lon=-75.1652")
    cel = response.json()['main']['temp']
    far = (float(cel)*9/5)+32
    l.append(far)
    l.append(response.json()['weather'][0]['main'])


    return l
