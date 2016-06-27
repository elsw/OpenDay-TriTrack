import socket
import time
import pigpio

class TCPSend:
    def __init__(self,pi):
        self.pi = pi
        self.TCP_IP = '10.0.0.1'
        self.TCP_PORT = 5005
        self.BUFFERSIZE = 1024

        self.LED_PIN = 3

        self.discNotice = False
        
        #self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #self.socket.connect((self.TCP_IP, self.TCP_PORT))
        
    def sendData(self,addr,number):
        try:
            self.socket.send('A'+str(addr)+'N'+str(number)+'E')

        except:
            try:
                self.pi.write(self.LED_PIN,0)
                self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.socket.connect((self.TCP_IP, self.TCP_PORT))
                self.socket.settimeout(5)
                self.pi.write(self.LED_PIN,1)
                print "connected"
                self.discNotice = False
            except:
                "disconnected"
                if not self.discNotice:
                    print "disconnected"
                    self.discNotice = True
                time.sleep(0.5)
                

