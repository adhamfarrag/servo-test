from gpiozero import AngularServo
from time import sleep

Angle = 37

servo = AngularServo(Angle, min_pulse_width=0.0005, max_pulse_width=0.0025)

while (True):
    servo.angle = 0
    sleep(2)
    servo.angle = 45
    sleep(2)
