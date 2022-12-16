import RPi.GPIO as GPIO
import time
import tkinter as tk
from sensor import distance


Motor1A = 8
Motor1B = 10
Motor1E = 12

Motor2A = 16
Motor2B = 18
Motor2E = 22

Trigger = 10
Echo = 8

# Confirugin the GPIO pins as outputs


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    GPIO.setup(Motor2E, GPIO.OUT)


def go_forward(tf):
    print("Going forward")

    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    time.sleep(tf)


def go_backward(tf):
    print("Going backwards")

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)

    time.sleep(tf)


def stop(tf):
    print("Now stop")

    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)
    time.sleep(tf)
    GPIO.cleanup()


def go_left(tf):
    print("Going left")

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    time.sleep(tf)


def go_right(tf):
    print("Going right")

    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)

    time.sleep(tf)


def key_input(event):

    print("Key:", event.char)
    key_press = event.char
    sleep_time = 0.060

    if key_press.lower() == "w":
        go_forward(sleep_time)
    elif key_press.lower() == "s":
        go_backward(sleep_time)
    elif key_press.lower() == "a":
        go_left(sleep_time)
    elif key_press.lower() == "d":
        go_right(sleep_time)
    elif key_press.lower() == "x":
        stop(sleep_time)
    else:
        pass

    curDis = distance("cm")
    print("Distance:", curDis)

    if curDis < 15:
        init()
        go_backward(0.5)


command = tk.TK()
command.bind('<keypress>', key_input)
command.mainloop()


GPIO.cleanup()
