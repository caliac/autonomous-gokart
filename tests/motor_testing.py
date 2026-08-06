#import lgpio as GPIO
import time
import hardware

driver1 = hardware.motor_driver.MotorDriver(RPWMpin=19, LPWMpin=13, R_ENpin=26, L_ENpin=5)
driver2 = hardware.motor_driver.MotorDriver(RPWMpin=12, LPWMpin=18, R_ENpin=16, L_ENpin=20)

motor1 = hardware.motor.Motor(driver1)
motor2 = hardware.motor.Motor(driver2)


try:
    print("Starting motor test.")

    motor1.set_speed(30)
    motor2.set_speed(30)
    time.sleep(2)

    motor1.set_speed(80)
    motor2.set_speed(80)
    time.sleep(4)

    motor1.set_speed(0)
    motor2.set_speed(0)
    time.sleep(1)

    motor1.set_speed(-30)
    motor2.set_speed(-30)
    time.sleep(2)

    motor1.set_speed(-100)
    motor2.set_speed(-100)
    time.sleep(3)

    motor1.set_speed(-50)
    motor2.set_speed(-50)
    time.sleep(2)

    motor1.set_speed(0)
    motor2.set_speed(0)

except KeyboardInterrupt:
    motor1.set_speed(0)
    motor2.set_speed(0)
    print("Interrupted by user")

finally:
    driver1.end()
    driver2.end()