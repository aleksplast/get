import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)
GPIO.setup(14, GPIO.OUT)
if GPIO.input(22) == GPIO.HIGH:
    GPIO.output(14, 1)
else:
    GPIO.output(14, 0)



