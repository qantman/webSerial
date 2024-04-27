import serial
import time


class SerialDataReceiver():
    def __init__(self, port:str='/dev/ttyUSB0', baudrate:int=9600) -> None:
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial = serial.Serial(self.port, self.baudrate)
        self.running = True
        time.sleep(2)

    def read(self):
        with self.serial as ser:
            if self.running:
                try:
                    data_str = str(ser.readline().decode('utf-8').strip())
                    return self.__parse__(data_str)
                except:
                    return "000;0:Error;1:Error;2:Error;3:Error;4:Error;5:Error;6:Error;7:Error"             

    def __parse__(self, string:str):
        parts = string.split(';')
        adress,  *values_str = parts
        obj = {
            "Adress":adress,
            "Data":{
            },
            "Values": [
            ]
        }
        for i in range(len(values_str)):
            id, value = values_str[i].split(":")
            obj["Data"][id] = value
            obj["Values"].append(value)

        return obj