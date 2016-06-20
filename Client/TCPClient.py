import socket

class TCPSend:
    def __init__(self):
        TCP_IP = '10.0.0.1'
        TCP_PORT = '5005'
        BUFFERSIZE = 1024

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        


    def test()
        s.connect((TCP_IP, TCP_PORT))
        s.send("test")
        s.close()

        print "done"




if __name__ = "__main__":
    t = TCPSend()
    t.test()
