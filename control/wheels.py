#rename this to something better later
#this file is for controlling the driving

class Wheels:

    def __init__(self, left_motor, right_motor): #motor 1(driver1(pin1, pin2, pin3, pin4)), motor 2(driver2(pin1, pin2, pin3, pin4))
        self.left_motor = left_motor
        self.right_motor = right_motor

    def forward(self, speed):
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

    def backward(self, speed):
        pass
        #maybe combine forward and backward into just drive(self, speed)

    def left(self, speed):
        pass

    def right(self, speed):
        pass

    def brake(self):
        self.left_motor.set_speed(0)
        self.right_motor.set_speed(0)