from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

while (True):
    servo.angle = 15
    sleep(1.5)
    servo.angle = 0
    sleep(1.5)
    servo.angle = 15
    sleep(1.5)