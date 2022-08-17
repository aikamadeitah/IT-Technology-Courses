import time
import serial
arduinoData=serial.Serial('com3',115200)
time.sleep(1)
while (1==1):
    while (arduinoData.inWaiting()==0):
        pass
    dataPacket = arduinoData.readline() #reply
    dataPacket=str(dataPacket,'utf-8')
    splitPacket=dataPacket.split(",")
    X=float(splitPacket[0])
    Y=float(splitPacket[1])
    Z=float(splitPacket[2])
    print ("X=",X," Y=",Y," Z=",Z)
