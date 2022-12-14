from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

while (True):
    # test values for a gripper servo
    servo.angle = 0
    sleep(1)
    servo.angle = 15
    sleep(1)
    servo.angle = 10
    sleep(1)
