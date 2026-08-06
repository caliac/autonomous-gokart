import lgpio as GPIO
import time

#set pins
TRIG = 23
ECHO = 24

#open GPIO chip and set GPIO direction
h = GPIO.gpiochip_open(4)
GPIO.gpio_claim_output(h, TRIG)
GPIO.gpio_claim_input(h, ECHO)

def get_distance():
    #set TRIG LOW
    GPIO.gpio_write(h, TRIG, 0)
    time.sleep(0.1)

    
    #send 10us pulse to TRIG
    GPIO.gpio_write(h, TRIG, 1)
    time.sleep(0.00001)
    GPIO.gpio_write(h, TRIG, 0)

    pulse_start = time.time()
    timeout = time.time() + 0.5

    #start recording the time when the wave is sent
    while GPIO.gpio_read(h, ECHO) == 0:
        pulse_start = time.time()
        if time.time() > timeout:
            return -1

    pulse_end = time.time()
    timeout = time.time() + 0.5

    while GPIO.gpio_read(h, ECHO) == 1:
        pulse_end = time.time() #record time of arrival
        if time.time() > timeout:
            return -1

    pulse_duration = pulse_end - pulse_start #calc diff in times

    

    distance = pulse_duration * 17150 #multiply with tonic speed (34300 cm/s) and div by 2 because there and back
    distance = round(distance, 2)

    return distance

if __name__ == "__main__":
    try:
        while True:
            dist = get_distance()
            if dist == -1:
                print("Sensor Timeout: Check your ECHO/TRIG wiring.", flush=True)
            else:
                if dist < 10:
                    print(f"Obstacle detected {dist} cm away")
                else:
                    print(f"Measured distance = {dist} cm")
            time.sleep(1)
    
    except KeyboardInterrupt: #reset by pressing ctrl+c
        print("\nMeasurement stopped by user", flush=True)
    finally:
        GPIO.gpiochip_close(h)
