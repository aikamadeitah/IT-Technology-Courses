import serial.tools.list_ports
import re

class port_lookup:

    def __init__(self) -> None:
        self.my_xbee="USB VID:PID=0403:6015 SER=D307.+"
        self.myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]

        if not self.myports:
            print("No device found")

    def find_xbee_port(self):
        xbee_port = ""

        for devices in self.myports:

            if re.search(self.my_xbee,devices[2]):
                print("Xbee device found on port:",devices[0])
                xbee_port = devices[0]
                break
            else:
                print("This device is not a xbee:",devices[1])
        
        return(xbee_port)
