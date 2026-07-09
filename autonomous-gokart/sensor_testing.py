""""


import lgpio as GPIO
import time

#set pins
TRIG = 23
ECHO = 24

#open GPIO chip and set GPIO direction
h = GPIO.gpiochip_open(0)
GPIO.gpio_claim_output(h, TRIG)
GPIO.gpio_claim_input(h, ECHO)

def get_distance():
    #set TRIG LOW
    GPIO.gpio_write(h, TRIG, 0)
    time.sleep(2)

    
    #send 10us pulse to TRIG
    GPIO.gpio_write(h, TRIG, 1)
    time.sleep(0.00001)
    GPIO.gpio_write(h, TRIG, 0)

    #start recording the time when the wave is sent
    while GPIO.gpio_read(h, ECHO) == 0:
        pulse.start = time.time()

    while GPIO.gpio_read(h, ECHO) == 1:
        pulse_end = time.time() #record time of arrival

    pulse_duration = pulse_end - pulse_start #calc diff in times

    

    distance = pulse_duration * 171150 #multiply with tonic speed (34300 cm/s) and div by 2 because there and back
    distance = round(distance, 2)

    return distance

if __name__ == "main":
    try:
        while True:
            dist = get_distance
            print("Measured distance = {:.2f} cm".format(dist))
            time.sleep(1)
    
    except KeyboardInterrupt: #reset by pressing ctrl+c
        print("Measurement stopped by user")
        GPIO.gpiochip_close(h)

"""
