import control
import hardware

import time

left_motor_driver = hardware.motor_driver.MotorDriver(RPWMpin=19, LPWMpin=13, R_ENpin=26, L_ENpin=5)
right_motor_driver = hardware.motor_driver.MotorDriver(RPWMpin=12, LPWMpin=18, R_ENpin=16, L_ENpin=20)

left_motor = hardware.motor.Motor(left_motor_driver)
right_motor = hardware.motor.Motor(right_motor_driver)

robot = control.wheels.Wheels(left_motor, right_motor)

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
time.sleep(1)
robot.end()

