#rename this to something better later
#this file is for controlling the driving

class Wheels:

    def __init__(self, left_motor, right_motor): #motor 1(driver1(pin1, pin2, pin3, pin4)), motor 2(driver2(pin1, pin2, pin3, pin4))
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.turning_constant = 10 #NOTE: change so that the non-turning-fast motor is turning at a fraction of the inputted speed rate of the turning-fast motor
                                            #otherwise if the turn speed is 5 then it wouldn't be turning the correct direction.

    def drive(self, speed):
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(speed)

    def left(self, speed):
        self.left_motor.set_speed(self.turning_constant)
        self.right_motor.set_speed(speed)

    def right(self, speed):
        self.left_motor.set_speed(speed)
        self.right_motor.set_speed(self.turning_constant)

    def brake(self):
        self.left_motor.set_speed(0)
        self.right_motor.set_speed(0)