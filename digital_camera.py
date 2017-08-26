import RPi.GPIO as GPIO
from time import sleep,time
from datetime import datetime
import subprocess
from os import system

#setting GPIObord
LED_PORT = 4
PE_PORT = 18
SWITCH_PORT = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PORT, GPIO.OUT)
GPIO.setup(PE_PORT, GPIO.OUT)
GPIO.setup(SWITCH_PORT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#run command
def exc(cmd):
    r = subprocess.check_output(cmd, shell=True)
    return r.decode("utf-8").strip()

#  run photo command
def take_photo():
    now = datetime.now()
    f = now.strftime('%Y-%m-%d-%H-%M-%S') + ".jpg" #  file name
    system("fswebcam -r 1280x1024 "+f)

#  beep buzeer
def beep():
    pwm = GPIO.PWM(PE_PORT, 330) #  pwm as beep command in f = 330
    pwm.start(50)
    sleep(0.1)
    pwm.ChangeFrequency(440)
    sleep(0.1)
    pwm.stop

#  what Rpi do when you push button
try:
    sw = 0
    while True:
        if GPIO.input(SWITCH_PORT) == GPIO.HIGH:
            # if sw != 0: continue #  aboid continuous shooting
            # sw = 1
            GPIO.output(LED_PORT, GPIO.HIGH)
            beep()
            take_photo()
            print("Finish, taking photo")
            continue
        else:
            sw = 0
            GPIO.output(LED_PORT, GPIO.LOW)
        sleep(0.1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()

