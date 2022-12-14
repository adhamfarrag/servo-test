from gpiozero import AngularServo
from time import sleep

servoOne = AngularServo(23, min_pulse_width=0.0006, max_pulse_width=0.0023)
servoTwo = AngularServo(24, min_pulse_width=0.0006, max_pulse_width=0.0023)


while (True):
    # test values for a gripper servo
    servoOne.angle = -90
    servoTwo.angle = -90
    sleep(4)
    servoOne.angle = 0
    servoTwo.angle = 0
    sleep(4)
    servoOne.angle = 90
    servoTwo.angle = 90
    sleep(4)

