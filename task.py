import RPi.GPIO as GPIO
#import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN)

GPIO.setup(22, GPIO.OUT)

ch15_state = GPIO.input(15)
GPIO.output(22, ch15_state)

#time.sleep(2)

#GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW)

#time.sleep(2)


#GPIO.setup(22, GPIO.OUT, initial = GPIO.HIGH)

#time.sleep(2)

#GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW)

#time.sleep(2)


