import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# t = input('time=')
t = 30
# f = input('f=')
# dc = input('dc=')
f = 200
dc = 70

p = GPIO.PWM(12, 1)  # channel=12 frequency=1Hz
p.start(100)

step = t*f
for i in range(1, step):
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.LOW)
    time.sleep(1.0*dc/100/f)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.HIGH)
    time.sleep(1.0*(100-dc)/100/f)

p.stop()
GPIO.cleanup()