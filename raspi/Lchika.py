import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

for i in range(10):
	GPIO.output(2,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(2,GPIO.LOW)
	time.sleep(0.1)

