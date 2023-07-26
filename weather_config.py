import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\SESA732254\PycharmProjects\pythonProject1\\build\exe.win-amd64-3.10')
from pyowm.owm import OWM
import config
import gui_loc
from time import *


def owm_connection():  # connecting to openweathermap.org
    owm = OWM(config.API_KEY)  # API key from openweathermap.org
    manager = owm.weather_manager()  # TODO: check
    # getting weather at coords from user -->
    place = manager.weather_at_coords(float(gui_loc.get_value()[0]), float(gui_loc.get_value()[1]))
    return [place, manager]  # return manager and weather at place


def get_weather():
    weathers = owm_connection()[0].weather  # getting current weather
    dump_dict = weathers.to_dict()  # convert weather information to dictionary
    return [dump_dict, weathers]  # return weather dict and current weather information


def forecast_seven_days():
    # getting 7 days forecast for every 3 hours
    results = []  # empty list
    seven_days_forcast = owm_connection()[1].forecast_at_coords(float(gui_loc.get_value()[0]),
                                                                float(gui_loc.get_value()[1]),
                                                                '3h').forecast  # forecast
    for weather in seven_days_forcast:  # loop
        results.append({f'{weather.status}': weather.reference_time('iso')})  # convert forecast to dictionary
    return results  # return forecast dict


def get_local_time():
    localtime_var = asctime(localtime(time()))  # get local time
    local_time_correct = localtime_var.split()  # spit local time by single space
    return local_time_correct  # return local time


def get_temperature():
    temperature = get_weather()[1].temperature('celsius')  # getting temperature
    return temperature['temp']  # return temperature


def get_sunrise():
    sunrise = strftime('%H:%M', gmtime(get_weather()[0]['sunrise_time'] + 10800))  # getting sunrise H and M
    return sunrise  # return sunrise H and M


def get_sunset():
    sunset = strftime('%H:%M', gmtime(get_weather()[0]['sunset_time'] + 10800))  # getting sunset H and M
    return sunset  # return sunrise H and M
