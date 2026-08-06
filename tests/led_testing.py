from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    for brightness in range(0, 101): #fades in
        led.value = brightness / 100
        sleep(0.02)
    for brightness in range(100, -1, -1): #fades out
        led.value = brightness / 100
        sleep(0.02)
