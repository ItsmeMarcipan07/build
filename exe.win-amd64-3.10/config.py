import sys
import pathlib

sys.path.insert(1, f"{pathlib.Path().resolve()}")
from data_from_user import data

# getting information from data_from_user.py

PLC_IP: str = str(data[0])  # get PLC IP
PLC_PORT: int = int(data[1])  # get PLC PORT
PLC_NAME: str = str(data[2])  # get PLC NAME
UNIT: int = data[3]  # get UNIT
API_KEY: str = str(data[4])  # get API KEY
Latitude: float = float(data[5])  # get latitude
Longitude: float = float(data[6])  # get logitude
