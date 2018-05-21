import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

try:
    GPIO.output(12, GPIO.HIGH)
    time.sleep(10)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

