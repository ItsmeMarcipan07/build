import sys
import pathlib
from tkinter import messagebox

sys.path.insert(1, f"{pathlib.Path().resolve()}")
messagebox.showinfo(title="INFO WINDOW", message=f"Connecting...\nClick OK!")
import modbus_protocols
import connection
from time import *

# while True:
#     try:
#         connection.connection_plc()  # calling function connection_plc
#         modbus_protocols.write_modbus()  # calling function write_modbus
#         modbus_protocols.read_modbus()  # calling function read_modbus
#         modbus_protocols.is_raining()  # calling function is_raining
#         print("The information was sent!")  # print
#     except OSError("Invalid data!") as e:
#         messagebox.showerror("Error", str(e))
#         raise ValueError("Invalid data!")  # raise an exception
#     sleep(15)  # sleep

while True:
    connection.connection_plc()  # calling function connection_plc
    modbus_protocols.write_modbus()  # calling function write_modbus
    modbus_protocols.read_modbus()  # calling function read_modbus
    modbus_protocols.is_raining()  # calling function is_raining
    sleep(15)  # sleep
