import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.setwarnings(False)

Forward_left=20
Backward_left=21
Forward_right = 16
Backward_right = 26

# Speed control
speed_low = 33
speed_med = 66
speed_high = 100
speed = speed_med

# Motor setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward_left, GPIO.OUT)
GPIO.setup(Backward_left, GPIO.OUT)
GPIO.setup(Forward_right, GPIO.OUT)
GPIO.setup(Backward_right, GPIO.OUT)

# PWM setup
pwm_frequency = 10000

pwm_forward_left = GPIO.PWM(Forward_left, pwm_frequency)
pwm_backward_left = GPIO.PWM(Backward_left, pwm_frequency)
pwm_forward_right = GPIO.PWM(Forward_right, pwm_frequency)
pwm_backward_right = GPIO.PWM(Backward_right, pwm_frequency)

pwm_forward_left.start(0)
pwm_backward_left.start(0)
pwm_forward_right.start(0)
pwm_backward_right.start(0)

def forward():
    pwm_forward_left.ChangeDutyCycle(speed)
    pwm_forward_right.ChangeDutyCycle(speed)

def backward():
    pwm_backward_left.ChangeDutyCycle(speed)
    pwm_backward_right.ChangeDutyCycle(speed)

def turn_right():
    pwm_backward_left.ChangeDutyCycle(speed)
    pwm_forward_right.ChangeDutyCycle(speed)

def turn_left():
    pwm_forward_left.ChangeDutyCycle(speed)
    pwm_backward_right.ChangeDutyCycle(speed)

def stop():
    pwm_forward_left.ChangeDutyCycle(0)
    pwm_forward_right.ChangeDutyCycle(0)
    pwm_backward_left.ChangeDutyCycle(0)
    pwm_backward_right.ChangeDutyCycle(0)

def set_speed_slow():
    global speed
    speed = speed_low

def set_speed_med():
    global speed
    speed = speed_med

def set_speed_fast():
    global speed
    speed = speed_high
