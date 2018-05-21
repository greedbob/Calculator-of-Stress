import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

# f = input('f')
# dc = input('dc')

p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)

try:
    p.ChangeDutyCycle(50)
    time.sleep(100)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
