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
