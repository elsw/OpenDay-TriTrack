import pigpio
from TCPClient import TCPSend

pi = pigpio.pi('localhost')
TCPSend = TCPSend(pi)

numberPins = [21,20,26,16,19,13,12,6,5,7]
addressPins = [8,11,25,9]
validPin = 10

address = 0
number = 0

values = [0,0,0,0,0,0,0,0]

while True:
    address = 0
    if pi.read(validPin):
        for i in range(len(addressPins)):
            address = address + (pi.read(addressPins[i])*pow(2,i))

        number = 0
        for i in range(len(numberPins)):
            number = number + (pi.read(numberPins[i])*pow(2,i))
            
        if pi.read(validPin):
            values[address] = number
            TCPSend.sendData(address,number)
        

    
        
        
