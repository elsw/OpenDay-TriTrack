import pigpio
import time
from Adafruit_PWM_Servo_Driver import PWM

class ServoDriver:
    def __init__(self):
        # Initialise the PWM device using the default address
        pwm = PWM(0x40)
        pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

        self.basePin = 3
        #self.baseMiddle = 365
        #self.base90 = 610
        self.baseMin = 150
        self.baseMax = 570
        self.shoulderPin = 4
        #self.shoulderMiddle = 410
        #self.shoudler90 = 190
        self.shoulderMin = 190
        self.shoulderMax = 600
        self.elbowPin = 5
        #self.elboxMiddle = 360
        #self.elbow90 = 580
        self.elboxMax = 700
        self.elbowMin = 360
        self.wristPin = 7
        #self.wristMiddle = 430
        #self.wrist90 = 150
        self.wristMin = 150
        self.wristMax = 700
        self.twistPin = 6
        #self.twistMiddle = 450
        #self.twistMin = 50
        self.twistMax = 700
        self.grabPin = 8
        #self.grabMiddle = 650
        self.grabMax = 800
        self.grabMin = 450
