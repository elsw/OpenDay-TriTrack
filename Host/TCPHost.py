import socket
import time
import pigpio

pi = pigpio.pi('localhost')
LED_PIN = 21

TCP_IP = '10.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))

running = True
connecting = True

while running:

    if connecting:
        print "listening"
        s.listen(1)

        conn, addr = s.accept()
        print "Connecttion from", addr
        connecting = False
        pi.write(LED_PIN,1)
    else:

        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                connecting = True
                pi.write(LED_PIN,0)
                break
            print "received data",data
            time.sleep(0.5)

print "connection closed"
conn.close()
