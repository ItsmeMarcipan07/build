import sys
import pathlib

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, f"{pathlib.Path().resolve()}")
import modbus_protocols
import connection
from time import *
import tkinter

while True:
    try:
        connection.connection_plc()  # calling function connection_plc
        modbus_protocols.write_modbus()  # calling function write_modbus
        modbus_protocols.read_modbus()  # calling function read_modbus
        modbus_protocols.is_raining()  # calling function is_raining
        print("The information was sent!")  # print
    except Exception:
        tkinter.messagebox.showerror("Error", str(e))
        raise ValueError("Invalid data!")  # raise an exception
    sleep(15)  # sleep
