#!/usr/bin/env python
import time
import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
while 1:
    x = ser.readline().strip()
    print(x)

if x == b"a":
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)
    time.sleep(1)
    print("RED LED ON")

if x == b"b":
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)
    time.sleep(1)
    print("YELLLO LED ON")

if x == b"hej":
    GPIO.output(26, GPIO.LOW)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(24, GPIO.LOW)
    time.sleep(1)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(24, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(24, GPIO.LOW)
    time.sleep(1)

else:
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    print("green on, all good")
    GPIO.output(26, GPIO.HIGH)
    print("LED OFF")