#!/usr/bin/env python3.7
from digi.xbee.devices import XBeeDevice

port="COM3" # Here you type in the serial port where your module is
connected.
baud_rate=9600 # Enter baud rate of your module here.
node_name="End_device" # Here you type in the node identifier.
send_message="a" # Here you enter the text to send.

def main():
    print("XBee Sending API Frame Data Sample")
    device = XBeeDevice(port, baud_rate)
    device.open()

    try:
        xnet = device.get_network()
        remote_device = xnet.discover_device(node_name)
        
        print("sending data to %s >> %s" %
        (remote_device.get_64bit_addr(),node_name))

        device.send_data(remote_device,send_message)
        print("success \n")

    finally:
        device.close()

if __name__ == '__main__':
    main()