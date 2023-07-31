import sys
import pathlib

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, f"{pathlib.Path().resolve()}")

# imports
from pymodbus.client import ModbusTcpClient as ModbusClient
import config
from tkinter import messagebox


def connection_plc():
    client = ModbusClient(config.PLC_IP, config.PLC_PORT)  # create modbus client with PLC_IP and PLC_PORT
    try:
        client.connect()  # create connection
        return client  # return connection
    except OSError("Fail to connect!") as oserr:
        messagebox.showerror("Connection error", str(oserr))
    # return client  # return connection


try:
    # check connection for errors
    connection_plc()  # connecting
    print("Connected!")  # print


except OSError("Invalid data!") as oserr:
    messagebox.showerror("Connection error", str(oserr))
    connection_plc().close()  # closing connection
    raise OSError("Invalid data!")  # raise an exception
