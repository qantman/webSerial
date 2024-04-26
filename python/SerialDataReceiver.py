import serial


class SerialDataReceiver():
    def __init__(self, port:str='/dev/ttyUSB0', baudrate:int=9600) -> None:
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial = serial.Serial(self.port, self.baudrate)
        self.running = True

    def read(self):
        with self.serial as ser:
            if self.running:
                data_str = ser.readline().decode('utf-8').strip()
                return self.__parse__(data_str)
                    
                    

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



