import pigpio
from TCPClient import TCPSend
import time

pi = pigpio.pi('localhost')
TCPSend = TCPSend(pi)

numberPins = [21,20,26,16,19,13,12,6,5,7]
addressPins = [8,11,25,9]
validPin = 10
readyPin = 24

address = 0
number = 0

values = [0,0,0,0,0,0,0,0]

pi.write(readyPin,0)

while True:

    while not pi.read(validPin):
        pass
 
    address = 0  
    for i in range(len(addressPins)):
        address = address + (pi.read(addressPins[i])*pow(2,i))

    number = 0
    for i in range(len(numberPins)):
        number = number + (pi.read(numberPins[i])*pow(2,i))
            
    values[address] = number
    TCPSend.sendData(address,number)

    #set ready signal
    pi.write(readyPin,1)

    #wait for valid signal rising edge
    while pi.read(validPin):
        pass
    #reset ready pin
    pi.write(readyPin,0)
        
        
