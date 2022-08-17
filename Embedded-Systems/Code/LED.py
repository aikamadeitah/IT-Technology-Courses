#!/usr/bin/env python
import time
import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)

#These lines just make our python program recognize where the XBEE module is and what settings it needs to send and receive messages

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=3
)
while 1 :
#This code reads for a message from the coordinator ‘b”a’. When the coordinator receives this message it turns the LED on.Otherwise the LED remains off.

    x=ser.readline().strip()
    if x == b"a":
        GPIO.output(23,GPIO.HIGH)
        time.sleep(1)
        print("LED ON")
    else:
        GPIO.output(23,GPIO.LOW)
        print ("LED OFF")