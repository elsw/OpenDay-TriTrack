import pigpio
import time
from Servo_Driver.Adafruit_PWM_Servo_Driver import PWM

class ServoDriver:
    def __init__(self):
        # Initialise the PWM device using the default address
        pwm = PWM(0x40)
        pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

        self.endOfAddr = False
        
        self.data = [0,0,0,0,0,0,0,0]

        self.basePin = 3
        self.baseInRange = [0,1024]
        self.baseArmRange = [150,570]
        self.shoulderPin = 4
        self.sholderInRange = [0,1024]
        self.shoulderArmRange = [190,600]
        self.elbowPin = 5
        self.elbowInRange = [0,1024]
        self.elboxArmRange = [360,700]
        self.wristPin = 7
        self.wristInRange = [0,1024]
        self.wristArmRange = [150,700]
        self.twistPin = 6
        self.twistInRange = [0,1024]
        self.twistArmRange = [50,700]
        self.grabPin = 8
        self.grabInRange = [0,1024]
        self.grabArmRange = [450,800]

    def addData(self,address,number):
        self.data[address] = number

        if address == 7:
            endOfAddr = True
        elif address == 1:
            if endOfAddr == True:
                endOfAddr = False
                #update servos
                self.__updateServos()

    def updateServos(self):
        

        
