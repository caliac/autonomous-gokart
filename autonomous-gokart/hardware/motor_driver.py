#motor driver class
import lgpio as GPIO

class MotorDriver:
    
    def __init__(self, RPWMpin, LPWMpin, R_ENpin, L_ENpin): #motor 1 had 18, 19, 23, 24
        self.RPWMpin = RPWMpin
        self.LPWMpin = LPWMpin
        self.R_ENpin = R_ENpin
        self.L_ENpin = L_ENpin

        self.freq = 2000 #Hz
        
        self.handle = GPIO.gpiochip_open(4) #raspberry pi 5 uses handle 4

        #set up output pins
        GPIO.gpio_claim_output(self.handle, self.R_ENpin)
        GPIO.gpio_claim_output(self.handle, self.RPWMpin)
        GPIO.gpio_claim_output(self.handle, self.L_ENpin)
        GPIO.gpio_claim_output(self.handle, self.LPWMpin)

        #enable motor driver
        GPIO.gpio_write(self.handle, self.R_ENpin, 1)
        GPIO.gpio_write(self.handle, self.L_ENpin, 1)

        #start with motor stopped
        GPIO.tx_pwm(self.handle, self.RPWMpin, self.freq, 0)
        GPIO.tx_pwm(self.handle, self.LPWMpin, self.freq, 0)

        print(f"Motor driver initialized, using RPWM = {self.RPWMpin}, LPWM = {self.LPWMpin}, R_EN = {self.R_ENpin}, L_EN = {self.L_ENpin}")

    def set_PWM(self, RPWMspeed, LPWMspeed):
        #clamps speed values
        RPWMspeed = int(RPWMspeed)
        RPWMspeed = max(0, min(100, RPWMspeed))
        LPWMspeed = int(LPWMspeed)
        LPWMspeed = max(0, min(100, LPWMspeed))

        GPIO.tx_pwm(self.handle, self.RPWMpin, self.freq, RPWMspeed)
        GPIO.tx_pwm(self.handle, self.LPWMpin, self.freq, LPWMspeed)

    def end(self):
        GPIO.tx_pwm(self.handle, self.RPWMpin, self.freq, 0)
        GPIO.tx_pwm(self.handle, self.LPWMpin, self.freq, 0)
        GPIO.gpio_write(self.handle, self.R_ENpin, 0)
        GPIO.gpio_write(self.handle, self.L_ENpin, 0)
        GPIO.gpiochip_close(self.handle)