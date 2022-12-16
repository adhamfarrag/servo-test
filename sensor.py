import RPi.GPIO as GPIO
import time

Trigger = 26
Echo = 24


def distance(measure='cm'):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Trigger, GPIO.OUT)
    GPIO.setup(Echo, GPIO.IN)

    time.sleep(0.3)
    GPIO.output(12, True)
    time.sleep(0.00001)

    GPIO.output(12, False)
    while GPIO.input(16) == 0:
        nosig = time.time()

    while GPIO.input(16) == 1:
        sig = time.time()

    tl = sig - nosig

    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print('Improper choice of measurement: in or cm')
        distance = None

    GPIO.cleanup()
    return distance


print(distance('cm'))
