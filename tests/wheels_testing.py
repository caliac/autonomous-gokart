from hardware import motor_driver
from hardware import motor
from control import wheels

import time

left_motor_driver = motor_driver.MotorDriver(RPWMpin=19, LPWMpin=13, R_ENpin=26, L_ENpin=5)
right_motor_driver = motor_driver.MotorDriver(RPWMpin=12, LPWMpin=18, R_ENpin=16, L_ENpin=20)

left_motor = motor.Motor(left_motor_driver)
right_motor = motor.Motor(right_motor_driver)

robot = wheels.Wheels(left_motor, right_motor)


try:
    robot.drive(20)
    time.sleep(2)
    robot.drive(50)
    time.sleep(2)
    robot.drive(-10)
    time.sleep(2)
    robot.right(30)
    time.sleep(1)
    robot.left(40)
    time.sleep(1)
    robot.brake()

except KeyboardInterrupt:
    robot.brake()

finally:
    robot.end()


