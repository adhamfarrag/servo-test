from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

while (True):
    # code to move side servo to 90 degrees
    servo.angle = 90
    sleep(1)
    # code to move side servo to 0 degrees
    servo.angle = 0
    sleep(1)
    # code to move side servo to 180 degrees
    servo.angle = 180
    sleep(1)
