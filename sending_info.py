# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\SESA732254\PycharmProjects\pythonProject1\\build\exe.win-amd64-3.10')
import modbus_protocols
import connection
from time import *

while True:
    try:
        connection.connection_plc()  # calling function connection_plc
        modbus_protocols.write_modbus()  # calling function write_modbus
        modbus_protocols.read_modbus()  # calling function read_modbus
        modbus_protocols.is_raining()  # calling function is_raining
        print("The information was sent!")  # print
    except Exception:
        raise OSError("Fail to connect!")  # raise an exception
    sleep(15)  # sleep
