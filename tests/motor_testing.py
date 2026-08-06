#import lgpio as GPIO
import time
from hardware.motor_driver import MotorDriver

driver1 = MotorDriver(RPWMpin=19, LPWMpin=13, R_ENpin=26, L_ENpin=5)
driver2 = MotorDriver(RPWMpin=12, LPWMpin=18, R_ENpin=16, L_ENpin=20)


try:
    print("Starting motor test.")

    driver1.set_speed(30)
    driver2.set_speed(30)
    time.sleep(2)

    driver1.set_speed(80)
    driver2.set_speed(80)
    time.sleep(4)

    driver1.set_speed(0)
    driver2.set_speed(0)
    time.sleep(1)

    driver1.set_speed(-30)
    driver2.set_speed(-30)
    time.sleep(2)

    driver1.set_speed(-100)
    driver2.set_speed(-100)
    time.sleep(3)

    driver1.set_speed(-50)
    driver2.set_speed(-50)
    time.sleep(2)

    driver1.set_speed(0)
    driver2.set_speed(0)

except KeyboardInterrupt:
    driver1.set_speed(0)
    driver2.set_speed(0)
    print("Interrupted by user")

finally:
    driver1.end()
    driver2.end()