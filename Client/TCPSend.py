import socket
import time 

class TCPSend:
    def __init__(self):
        self.TCP_IP = '10.0.0.1'
        self.TCP_PORT = 5005
        self.BUFFERSIZE = 1024

        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        


    def test(self):
        self.socket.connect((self.TCP_IP, self.TCP_PORT))
        self.socket.send("test")
        time.sleep(0.5)
        self.socket.send("test")
        self.socket.close()

        print "done"




if __name__ == "__main__":
    t = TCPSend()
    t.test()
