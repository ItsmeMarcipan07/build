import sys
import pathlib

sys.path.insert(1, f"{pathlib.Path().resolve()}")
from pymodbus.client import ModbusTcpClient as ModbusClient
import config
from tkinter import messagebox


def connection_plc():
    client = ModbusClient(config.PLC_IP, config.PLC_PORT)  # create modbus client with PLC_IP and PLC_PORT
    client.connect()  # create connection
    return client  # return connection


try:
    # check connection for errors
    connection_plc()  # connecting
    messagebox.showinfo(title="INFO WINDOW", message="Connected!")  # messagebox
    print("Connected!")  # print

except Exception:
    messagebox.showerror("Error", str(e))  # messagebox
    connection_plc().close()  # closing connection
    raise OSError("Fail to connect!")  # raise an exception
