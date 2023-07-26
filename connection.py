import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'C:\\Users\SESA732254\PycharmProjects\pythonProject1\\build\exe.win-amd64-3.10')
from pymodbus.client import ModbusTcpClient as ModbusClient
import config


def connection_plc():
    client = ModbusClient(config.PLC_IP, config.PLC_PORT)  # create modbus client with PLC_IP and PLC_PORT
    client.connect()  # create connection
    return client  # return connection


try:
    # check connection for errors
    connection_plc()  # connecting
    print("Connected!")  # print


except Exception:
    connection_plc().close()  # closing connection
    raise OSError("Fail to connect!")  # raise an exception
