import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
pwm = GPIO.PWM(32, 50)
pwm.start(7.5)
time.sleep(2)
pwm.ChangeDutyCycle(7)
time.sleep(2)
pwm.ChangeDutyCycle(12.5)
time.sleep(2)
pwm.ChangeDutyCycle(2.5)
time.sleep(2)

# (0,12.5) - (180,12.5)