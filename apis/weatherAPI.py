import requests

def get_weather_stats(city):
    response1 = requests.get('https://geocoding-api.open-meteo.com/v1/search?name='+city+'&count=1')
    lat = response1.json()['results'][0]['latitude']
    lon = response1.json()['results'][0]['longitude']
    response2 = requests.get('https://api.open-meteo.com/v1/forecast?latitude='+str(lat)+'&longitude='+str(lon)+'&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=Australia%2FSydney')
    return (response2.json()['daily']['temperature_2m_max'],response2.json()['daily']['temperature_2m_min'])

def get_airquality_stats(city):
    response1 = requests.get('https://geocoding-api.open-meteo.com/v1/search?name='+city+'&count=1')
    lat = response1.json()['results'][0]['latitude']
    lon = response1.json()['results'][0]['longitude']
    response2 = requests.get('https://air-quality-api.open-meteo.com/v1/air-quality?latitude='+str(lat)+'&longitude='+str(lon)+'&hourly=pm10,pm2_5')
    return (response2.json()['hourly']['pm10'],response2.json()['hourly']['pm2_5'])

# if __name__ == '__main__':
#     print(get_weather_stats("delhi"))