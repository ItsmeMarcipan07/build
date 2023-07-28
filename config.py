import sys
import pathlib

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, f"{pathlib.Path().resolve()}")
from data_from_user import data

# getting information from data_from_user.py

PLC_IP = str(data[0])  # get PLC IP
PLC_PORT = int(data[1])  # get PLC PORT
PLC_NAME = str(data[2])  # get PLC NAME
UNIT = data[3]  # get UNIT
API_KEY = str(data[4])  # get API KEY
Latitude = float(data[5])  # get latitude
Longitude = float(data[6])  # get logitude
