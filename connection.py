import sys
import pathlib

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, f"{pathlib.Path().resolve()}")
from pymodbus.client import ModbusTcpClient as ModbusClient
import config
import tkinter


def connection_plc():
    client = ModbusClient(config.PLC_IP, config.PLC_PORT)  # create modbus client with PLC_IP and PLC_PORT
    client.connect()  # create connection
    return client  # return connection


try:
    # check connection for errors
    connection_plc()  # connecting
    print("Connected!")  # print


except Exception:
    tkinter.messagebox.showerror("Error", str(e))
    connection_plc().close()  # closing connection
    raise OSError("Fail to connect!")  # raise an exception
