import sys
import pathlib

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, f"{pathlib.Path().resolve()}")
import connection
import weather_config
import config


def write_modbus():
    # sending information/write #
    sunrise_hour_write = connection.connection_plc().write_registers(0x000,
                                                                     int(weather_config.get_sunrise().split(":")[0]),
                                                                     unit=config.UNIT)
    sunrise_minutes_write = connection.connection_plc().write_registers(0x001,
                                                                        int(weather_config.get_sunrise().split(":")[1]),
                                                                        unit=config.UNIT)
    sunset_hour_write = connection.connection_plc().write_registers(0x002,
                                                                    int(weather_config.get_sunset().split(":")[0]),
                                                                    unit=config.UNIT)
    sunset_minutes_write = connection.connection_plc().write_registers(0x003,
                                                                       int(weather_config.get_sunset().split(":")[1]),
                                                                       unit=config.UNIT)
    current_temperature_write = connection.connection_plc().write_registers(0x004,
                                                                            int(weather_config.get_temperature()),
                                                                            unit=config.UNIT)
    local_hour_write = connection.connection_plc().write_registers(0x005,
                                                                   int(weather_config.get_local_time()
                                                                       [3].split(":")[0]),
                                                                   unit=config.UNIT)
    local_minutes_write = connection.connection_plc().write_registers(0x006,
                                                                      int(weather_config.get_local_time()
                                                                          [3].split(":")[1]),
                                                                      unit=config.UNIT)

    return [sunrise_hour_write, sunrise_minutes_write, sunset_hour_write, sunset_minutes_write,
            current_temperature_write, local_hour_write, local_minutes_write]  # return information


def read_modbus():
    # reading information/read #
    sunrise_hour_read = connection.connection_plc().read_holding_registers(0x000, 1, unit=config.UNIT)
    sunrise_minutes_read = connection.connection_plc().read_holding_registers(0x001, 1, unit=config.UNIT)
    sunset_hour_read = connection.connection_plc().read_holding_registers(0x002, 1, unit=config.UNIT)
    sunset_minutes_read = connection.connection_plc().read_holding_registers(0x003, 1, unit=config.UNIT)
    current_temperature_read = connection.connection_plc().read_holding_registers(0x004, 1, unit=config.UNIT)
    local_hour_read = connection.connection_plc().read_holding_registers(0x005, 1, unit=config.UNIT)
    local_minutes_read = connection.connection_plc().read_holding_registers(0x006, 1, unit=config.UNIT)

    return [sunrise_hour_read, sunrise_minutes_read, sunset_hour_read, sunset_minutes_read,
            current_temperature_read, local_hour_read, local_minutes_read]  # return information


def is_raining():
    ...
    # check current weather status
    # if weather_config.get_weather()[1].status == "Rain":
    #     read_coil = connection.connection_plc().write_coil(0, True, unit=config.UNIT)
    #
    # else:
    #     read_coil = connection.connection_plc().write_coil(0, False, unit=config.UNIT)
    # reading = connection.connection_plc().read_coils(0, 1, unit=config.UNIT)
    #
    # return [reading, read_coil]  # return information
