import socket
import time
import pigpio

class TCPSend:
    def __init__(self,pi):
        self.pi = pi
        self.TCP_IP = '10.0.0.1'
        self.TCP_PORT = 5005
        self.BUFFERSIZE = 1024

        self.LED_PIN = 21

        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
    def sendData(self,addr,number):
        try:
            self.socket.send("A")
            self.socket.send(addr)
            self.socket.send(number)
        except:
            print "connecting"
            try:
                self.socket.connect((self.TCP_IP, self.TCP_PORT))
                ##connected enable LED
                self.pi.write(self.LED_PIN,1)
            except:
                #cant connect, host down? disable LED
                self.pi.write(self.LED_PIN,0)

    def test(self):
        self.socket.connect((self.TCP_IP, self.TCP_PORT))
        self.pi.write(self.LED_PIN,1)
        self.socket.send("test")
        time.sleep(0.5)
        self.socket.send("test")
        self.socket.close()
        self.pi.write(self.LED_PIN,0)

        print "done"
    



if __name__ == "__main__":
    t = TCPSend(pigpio.pi('localhost'))
    t.test()
