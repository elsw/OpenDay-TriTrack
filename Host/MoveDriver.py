import pigpio
import time
from Servo_Driver.Adafruit_PWM_Servo_Driver import PWM

class MoveDriver:
    def __init__(self):
        # Initialise the PWM device using the default address
        self.pwm = PWM(0x40)
        self.pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

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
        self.grabAddress = 2
        self.grabInRange = [813,1024]
        self.grabArmRange = [450,800]

    def addData(self,address,number):
        self.data[address] = number
        print address
        if address == 7:
            self.endOfAddr = True
        elif address == 2:
            if self.endOfAddr == True:
                self.endOfAddr = False
                #update servos
                self.__updateServos()

    def __updateServos(self):
        #grabber
        num = self.__clamp(self.data[self.grabAddress],self.grabInRange[0],self.grabInRange[1])
        x = float(num - self.grabInRange[0])/float(self.grabInRange[1] - self.grabInRange[0])
        x = -x + 1 # invert scale
        pwmX = self.grabArmRange[0] + (x*float(self.grabArmRange[1] - self.grabArmRange[0]))
        self.pwm.setPWM(self.grabPin, 0,int(pwmX))
        #print pwmX
        


    def __clamp(self,x,min,max):
        if x < min:
            return min
        if x > max:
            return max
        return x





        

        
