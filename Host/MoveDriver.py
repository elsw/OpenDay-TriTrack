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
        self.baseAddress = 7
        self.baseInRange = [37,540]
        self.baseArmRange = [150,570]
        self.shoulderPin = 4
        self.shoulderAddress = 6
        self.shoulderInRange = [0,575]
        self.shoulderArmRange = [190,600]
        self.elbowPin = 5
        self.elbowAddress = 5
        self.elbowInRange = [5,300]
        self.elbowArmRange = [360,650]
        self.wristPin = 7
        self.wristAddress = 4
        self.wristInRange = [0,800]
        self.wristArmRange = [100,700]
        self.twistPin = 6
        self.twistAddress = 3
        self.twistInRange = [475,1024]
        self.twistArmRange = [81,514]
        self.grabPin = 8
        self.grabAddress = 2
        self.grabInRange = [813,1024]
        self.grabArmRange = [450,800]

    def addData(self,address,number):
        self.data[address] = number
        if address == 7:
            self.endOfAddr = True
        elif address == 2:
            if self.endOfAddr == True:
                self.endOfAddr = False
                #update servos after every full cycle
                self.__updateServos()

    def __updateServos(self):
        #grabber
        num = self.__clamp(self.data[self.grabAddress],self.grabInRange[0],self.grabInRange[1])
        x = float(num - self.grabInRange[0])/float(self.grabInRange[1] - self.grabInRange[0])
        x = -x + 1 # invert scale
        pwmX = self.grabArmRange[0] + (x*float(self.grabArmRange[1] - self.grabArmRange[0]))
        self.pwm.setPWM(self.grabPin, 0,int(pwmX))
        #twist
        num = self.__clamp(self.data[self.twistAddress],self.twistInRange[0],self.twistInRange[1])
        x = float(num - self.twistInRange[0])/float(self.twistInRange[1] - self.twistInRange[0])
        pwmX = self.twistArmRange[0] + (x*float(self.twistArmRange[1] - self.twistArmRange[0]))
        self.pwm.setPWM(self.twistPin, 0,int(pwmX))
        #wrist
        num = self.__clamp(self.data[self.wristAddress],self.wristInRange[0],self.wristInRange[1])
        x = float(num - self.wristInRange[0])/float(self.wristInRange[1] - self.wristInRange[0])
        x = -x + 1 # invert scale
        pwmX = self.wristArmRange[0] + (x*float(self.wristArmRange[1] - self.wristArmRange[0]))
        self.pwm.setPWM(self.wristPin, 0,int(pwmX))
        #elbow
        num = self.__clamp(self.data[self.elbowAddress],self.elbowInRange[0],self.elbowInRange[1])
        x = float(num - self.elbowInRange[0])/float(self.elbowInRange[1] - self.elbowInRange[0])
        pwmX = self.elbowArmRange[0] + (x*float(self.elbowArmRange[1] - self.elbowArmRange[0]))
        self.pwm.setPWM(self.elbowPin, 0,int(pwmX))
        #print pwmX
        #shoulder
        num = self.__clamp(self.data[self.shoulderAddress],self.shoulderInRange[0],self.shoulderInRange[1])
        x = float(num - self.shoulderInRange[0])/float(self.shoulderInRange[1] - self.shoulderInRange[0])
        pwmX = self.shoulderArmRange[0] + (x*float(self.shoulderArmRange[1] - self.shoulderArmRange[0]))
        self.pwm.setPWM(self.shoulderPin, 0,int(pwmX))
        #base
        num = self.__clamp(self.data[self.baseAddress],self.baseInRange[0],self.baseInRange[1])
        x = float(num - self.baseInRange[0])/float(self.baseInRange[1] - self.baseInRange[0])
        x = -x + 1 # invert scale
        pwmX = self.baseArmRange[0] + (x*float(self.baseArmRange[1] - self.baseArmRange[0]))
        self.pwm.setPWM(self.basePin, 0,int(pwmX))
        


    def __clamp(self,x,min,max):
        if x < min:
            return min
        if x > max:
            return max
        return x





        

        
