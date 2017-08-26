import RPi.GPIO as GPIO
import time

#  define bord number
SWITCH = 18
LED = 21

# format GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

#  turn off LED
GPIO.output(LED, GPIO.LOW)

try:
    #  comform status of switch
    while True:
        if  (GPIO.input(SWITCH) == GPIO.HIGH) :
            print('high')
            GPIO.output(LED, GPIO.HIGH)
        else:
            print('low')
            GPIO.output(LED, GPIO.LOW)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()

            
