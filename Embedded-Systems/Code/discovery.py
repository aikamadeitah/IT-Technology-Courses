import RPi.GPIO as GPIO
from digi.xbee.devices import XBeeDevice
from digi.xbee.models.status import NetworkDiscoveryStatus

# used serial port on RPi
PORT = "/dev/ttyUSB0" 

# baud rate of the devices
BAUD_RATE = 9600      

# GPIO 18 on RPi
led = 12             

GPIO.setwarnings(False)

# PAN ID for the coordinator
REMOTE_ID = "Coordinator" 


# information for the endpoint
end_device = XBeeDevice(PORT, BAUD_RATE) 



# function for the userinput on the coordinator side of the code. When the user writes 1/0. Data will be sent to the coordinator when the LED is on/off
def data_receive_callback(xbee_message): 
    xbee_network = end_device.get_network()
    remote_device = xbee_network.discover_device(REMOTE_ID)
    print(xbee_message.data.decode())
    if xbee_message.data.decode() == "1":
        print("The LED is ON")
        GPIO.output(led, GPIO.HIGH)
        end_device.send_data_async(remote_device, "Message from Endpoint: You just turned the LED ON")
    elif xbee_message.data.decode() == "0":
        GPIO.output(led, GPIO.LOW)
        end_device.send_data_async(remote_device, "Message from Endpoint...: You just turned the LED OFF")
        print("The LED is OFF")
    else:
        print("Unrecognized input")


# indicates the setup for the RPi.
def setup(): 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.LOW)
            

# "Waiting for data" messege when the code is running and waiting for data received.
def main():
    
    try:
        end_device.open()
        end_device.add_data_received_callback(data_receive_callback)
        
        print("Waiting for data...\n")
        input()
        
            
# stop when the needed information is received
    finally:
        if end_device is not None and end_device.is_open():
            end_device.close()

def destroy():
    GPIO.output(14, GPIO.LOW)
    GPIO.cleanup()    #CTRL+C
    exit()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()