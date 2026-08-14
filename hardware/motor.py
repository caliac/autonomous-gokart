#motor class
#from motor_driver import MotorDriver

class Motor:
    def __init__(self, driver):
        self.driver = driver
        print("Motor initialized.")

    def set_speed(self, speed):
        print(f"Setting speed of motor to {speed}.")
        speed = int(speed)
        speed = max(-100, min(100, speed))

        if speed > 0:
            #clockwise
            self.driver.set_PWM(RPWMspeed=speed, LPWMspeed=0)
        elif speed < 0:
            #counterclockwise
            flipped_speed = abs(speed)
            self.driver.set_PWM(RPWMspeed=0, LPWMspeed=flipped_speed)
        else: #else, speed = 0
            self.driver.set_PWM(RPWMspeed=0, LPWMspeed=0)

    def end(self):
        print("Ending motor.")
        self.driver.set_PWM(RPWMspeed=0, LPWMspeed = 0)
        self.driver.end()