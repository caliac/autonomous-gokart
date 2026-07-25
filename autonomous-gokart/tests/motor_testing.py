import lgpio as GPIO
import time

class Driver:
    def __init__(self):
        self.RPWM = 18 #this pin supports PWM
        self.LPWM = 19 #this pin supports PWM
        self.R_EN = 23
        self.L_EN = 24

        self.freq = 1000
        

        self.handle = GPIO.gpiochip_open(4) #raspberry pi 5 uses handle 4

        #set up output pins
        GPIO.gpio_claim_output(self.handle, self.R_EN)
        GPIO.gpio_claim_output(self.handle, self.RPWM)
        GPIO.gpio_claim_output(self.handle, self.L_EN)
        GPIO.gpio_claim_output(self.handle, self.LPWM)

        #enable motor driver
        GPIO.gpio_write(self.handle, self.R_EN, 1)
        GPIO.gpio_write(self.handle, self.L_EN, 1)

        #start with motor stopped
        GPIO.tx_pwm(self.handle, self.RPWM, self.freq, 0)
        GPIO.tx_pwm(self.handle, self.LPWM, self.freq, 0)

        print("Motor driver initialized")


    def set_speed(self, speed):
        speed = int(speed)
        speed = max(-100, min(100, speed))

        if speed > 0: #clockwise
            GPIO.tx_pwm(self.handle, self.LPWM, self.freq, 0) #stop left PWM
            GPIO.tx_pwm(self.handle, self.RPWM, self.freq, speed) #begin right PWM

            print(f"Spinning clockwise at {speed}% speed.")

        elif speed < 0: #counterclockwise
            ccspeed = abs(speed)
            GPIO.tx_pwm(self.handle, self.RPWM, self.freq, 0) #stop right PWM
            GPIO.tx_pwm(self.handle, self.LPWM, self.freq, ccspeed) #begin left PWM

            print(f"Spinning counter-clockwise at {ccspeed}% speed.")

        else: #else, speed is 0 -> stops motor

            #parameters of tx_pwm: handle, GPIO pin, frequency, duty cycles (0 = on HIGH 0% of the time)
            GPIO.tx_pwm(self.handle, self.RPWM, self.freq, 0)
            GPIO.tx_pwm(self.handle, self.LPWM, self.freq, 0)
            print("Motor stopped.")


    def end(self):
        print("Shutting down motor")
        GPIO.tx_pwm(self.handle, self.RPWM, self.freq, 0)
        GPIO.tx_pwm(self.handle, self.LPWM, self.freq, 0)
        GPIO.gpio_write(self.handle, self.R_EN, 0)
        GPIO.gpio_write(self.handle, self.L_EN, 0)
        GPIO.gpiochip_close(self.handle)

        print("Cleanup complete")

my_driver = Driver()

try:
    print("Starting motor test.")

    my_driver.set_speed(10)
    time.sleep(2)

    my_driver.set_speed(0)
    time.sleep(1)

    my_driver.set_speed(-10)
    time.sleep(2)

    my_driver.set_speed(0)

except KeyboardInterrupt:
    my_driver.set_speed(0)
    print("Interrupted by user")

finally:
    my_driver.end()
    print("the end!")