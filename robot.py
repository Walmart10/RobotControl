import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class Robot:
    def __init__(self, leftPins, rightPins, leftEn, rightEn):
        super().__init__()
        
        self.leftPins = leftPins
        self.rightPins = rightPins
        self.leftEn = leftEn
        self.rightEn = rightEn
        
    def turnOnEnable(self):
        GPIO.output(self.leftEn, 1)
        GPIO.output(self.rightEn, 1)
        
    def turnOffEnable(self):
        GPIO.output(self.leftEn, 0)
        GPIO.output(self.rightEn, 0)
        
    def isMoving(self):
        pins = self.leftPins + self.rightPins
        for 
    
    def forward(self):

    def backward(self):

    def left(self):

    def right(self):

    def stop(self):
