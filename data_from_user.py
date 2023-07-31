import sys
import pathlib

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, f"{pathlib.Path().resolve()}")

# getting settings from settings.txt

data = []  # empty var/list

with open("settings.txt") as MyFile:  # open settings file
    for line in MyFile:  # loop
        data.append(line.split()[-1])  # getting information
