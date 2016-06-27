import socket
import time
import pigpio
from MoveDriver import MoveDriver

pi = pigpio.pi('localhost')
LED_PIN = 21

TCP_IP = '10.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 32#1024
str_buffer = ""

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.settimeout(5)
s.bind((TCP_IP,TCP_PORT))

moveDriver = MoveDriver()

running = True
connecting = True

def processData(s):
    p = s.find('N')
    address = int(s[1:p])
    number = int(s[p+1:len(s)-1])
    moveDriver.addData(address,number)
    

while running:

    if connecting:
        print "listening"
        s.listen(1)
        try:
            conn, addr = s.accept()
            conn.settimeout(5)
            print "Connecttion from", addr
            connecting = False
            pi.write(LED_PIN,1)
        except:
            pass
    else:

        while 1:
            try:
                data = conn.recv(BUFFER_SIZE)
            except:
                connecting = True
                conn.close()
                pi.write(LED_PIN,0)
                break
            
            if not data:
                connecting = True
                conn.close()
                pi.write(LED_PIN,0)
                break
            
            #print data
            
            if not data[0] == 'A':
                #have only second half of a message
                #use previously saved str_buffer
                pos = data.find('E')
                processData(str_buffer + data[0:pos+1])
                #delete string
                data = data[pos + 1:]

            dataRemaining = True    
            while dataRemaining:
                pos = data.find('E')
                if pos == -1:
                    #no more data so leave
                    dataRemaining = False
                    #save the rest of the message, might be half of the next one
                    str_buffer = data
                else:
                    #process string
                    processData(data[0:pos+1])
                    #delete string
                    data = data[pos + 1:]
                
                    
            

print "connection closed"
conn.close()


