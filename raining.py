import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\SESA732254\PycharmProjects\pythonProject1\\build\exe.win-amd64-3.10')
import weather_config

raining_days = []  # empty var
for el in forecast_seven_days():  # loop
    for key, value in el.items():  # loop
        if "Rain" == key:  # check
            raining_days.append(value.split(":"))  # getting information
