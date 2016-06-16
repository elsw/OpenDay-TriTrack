import pigpio
import time


class ServoDriver:
    def __init__(self):
        
        self.servoPin = 21
        self.pwmCenter = 2050
        self.pwm120 = 845
        self.pwmFrequency = 50

        self.maxAngle = 160
        self.minAngle = -160

        
        self.pi = pigpio.pi('localhost')
        self.pi.set_PWM_frequency(self.servoPin,self.pwmFrequency)
        

    def setAngle(self,angle):
        a = self.__circularClamp(angle)
        pwm = self.pwmCenter + ((float(a)/120.0) * (self.pwm120-self.pwmCenter))
        self.pi.set_servo_pulsewidth(self.servoPin,pwm)
    def setPWM(self,pwm):
        self.pi.set_servo_pulsewidth(self.servoPin,pwm)

    def __circularClamp(self,angle):
        if angle > self.maxAngle:
            if angle - 360 > self.minAngle:
                return angle - 360
            else:
                self.maxAngle
        if angle < self.minAngle:
            if angle + 360 < self.maxAngle:
                return angle + 360
            else:
                return self.minAngle
        return angle

    def cleanup(self):
        pass
        #pigpio.stop()

    
if __name__ == "__main__":
    s = ServoDriver()
    s.setAngle(120)
    #time.sleep(3)
    #s.setAngle(90)
    s.cleanup()
    

        
        
