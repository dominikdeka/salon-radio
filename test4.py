import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def change(channel):
    print("%s ch%s is %s" % (datetime.now().strftime("%H:%M:%S.%f"), channel, GPIO.input(channel)))

GPIO.add_event_detect(23, GPIO.BOTH, callback=change)

time.sleep(100)
GPIO.cleanup()
