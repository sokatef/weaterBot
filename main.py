import requests
from config import weatherApiTpken
from config import weatherApiEndpoint

def getCurrentWeater(city):
    queryParams={"key": weatherApiTpken, "q": city}
    currentWeaterResponse=requests.get(weatherApiEndpoint+'current.json',queryParams)

    if currentWeaterResponse.status_code==200:
        return ( {"city":currentWeaterResponse.json()['location']['name'],"localTime":  currentWeaterResponse.json()['location']['localtime'],
            "currentTemperature": currentWeaterResponse.json()['current']['temp_c'],"feelsLike": currentWeaterResponse.json()['current']['feelslike_c'] , "windSpeed": currentWeaterResponse.json()['current']['wind_kph'],
            "windDirection": currentWeaterResponse.json()['current']['wind_dir'] ,"cloud": currentWeaterResponse.json()['current']['cloud'], "airHumidity": currentWeaterResponse.json()['current']['humidity'], "textDescription": currentWeaterResponse.json()['current']['condition']['text'] })
    #Температура в градусах Цельсия.
    # Скорость ветра в км/ч. Сам enum ветров тут https://www.surfertoday.com/windsurfing/how-to-read-wind-direction

    else:
        if (currentWeaterResponse.status_code==400 and currentWeaterResponse.json()['error']['code']=='406'):
            return 'Invalid location'
        else: return 'Bad request'
def getWeatherForNextThreeDays(city):
    queryParams={"key": weatherApiTpken, "q": city, "days": 3}
    currentWeaterResponse=requests.get(weatherApiEndpoint+'forecast.json',queryParams)
    if currentWeaterResponse.status_code==200:         
            a = {"day1":{"date":currentWeaterResponse.json()['forecast']['forecastday'][0]['date'],
                     "averageTemp":currentWeaterResponse.json()['forecast']['forecastday'][0]['day']['avgtemp_c'],
                     "averageWindSpeed":currentWeaterResponse.json()['forecast']['forecastday'][0]['day']['maxwind_kph'],
                     "averageHumidity":currentWeaterResponse.json()['forecast']['forecastday'][0]['day']['avghumidity'],
                     "chanceOfRain":currentWeaterResponse.json()['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],
                     "chanceOfSnow":currentWeaterResponse.json()['forecast']['forecastday'][0]['day']['daily_chance_of_snow']},
                 "day2":{"date":currentWeaterResponse.json()['forecast']['forecastday'][1]['date'],
                     "averageTemp":currentWeaterResponse.json()['forecast']['forecastday'][1]['day']['avgtemp_c'],
                     "averageWindSpeed":currentWeaterResponse.json()['forecast']['forecastday'][1]['day']['maxwind_kph'],
                     "averageHumidity":currentWeaterResponse.json()['forecast']['forecastday'][1]['day']['avghumidity'],
                     "chanceOfRain":currentWeaterResponse.json()['forecast']['forecastday'][1]['day']['daily_chance_of_rain'],
                     "chanceOfSnow":currentWeaterResponse.json()['forecast']['forecastday'][1]['day']['daily_chance_of_snow']},
                 "day3":{"date":currentWeaterResponse.json()['forecast']['forecastday'][2]['date'],
                     "averageTemp":currentWeaterResponse.json()['forecast']['forecastday'][2]['day']['avgtemp_c'],
                     "averageWindSpeed":currentWeaterResponse.json()['forecast']['forecastday'][2]['day']['maxwind_kph'],
                     "averageHumidity":currentWeaterResponse.json()['forecast']['forecastday'][2]['day']['avghumidity'],
                     "chanceOfRain":currentWeaterResponse.json()['forecast']['forecastday'][2]['day']['daily_chance_of_rain'],
                     "chanceOfSnow":currentWeaterResponse.json()['forecast']['forecastday'][2]['day']['daily_chance_of_snow']}}
            return a
    else:
        if (currentWeaterResponse.status_code==400 and currentWeaterResponse.json()['error']['code']=='406'):
            return 'Invalid location'
        else: return 'Bad request'
