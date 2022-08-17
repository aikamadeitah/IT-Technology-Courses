from digi.xbee.devices import XBeeDevice

# TODO: Replace with the serial port where your local module is connected to.
PORT = "COM7"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

DATA_TO_SEND = "Yeah I got it set up finally"
REMOTE_NODE_ID = "Thobias"


def main():
    print(" +-----------------------------------------------------+")
    print(" | XBee Python Library Send Data Asynchronously Sample |")
    print(" +-----------------------------------------------------+\n")

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        # Obtain the remote XBee device from the XBee network.
        xbee_network = device.get_network()
        remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
        if remote_device is None:
            print("Could not find the remote device")
            exit(1)

        print("Sending data asynchronously to %s >> %s..." % (remote_device.get_64bit_addr(), DATA_TO_SEND))

        device.send_data_async(remote_device, DATA_TO_SEND)

        print("Success")

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()