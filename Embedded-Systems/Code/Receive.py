#!/usr/bin/env python3.7
#import RPi.GPIO as GPIO
import time
from digi.xbee.devices import XBeeDevice

PORT = "COM4" # Here you type in the serial port where your module is connected.
BAUD_RATE = 9600 # Enter baud rate of your module here.

def data_receive_callback(xbee_message):
    print("Message: ", xbee_message.data.decode())
    xbeedata = xbee_message.data.decode()

if xbeedata == "a":
    #GPIO.output(23,GPIO.HIGH)
    time.sleep(1)
    print("LED ON")

elif xbeedata == "b":
    #GPIO.output(23,GPIO.LOW)
    time.sleep(1)
    print("LED OFF")


def main():
    device = XBeeDevice(PORT, BAUD_RATE)
    try:
        device.open()
        device.add_data_received_callback(data_receive_callback)
        print("Waiting for data...\n")

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == "__main__":
    print("Starting to receive")
    try:
        main()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        device.close()