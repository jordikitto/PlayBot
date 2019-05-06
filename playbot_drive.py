import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.setwarnings(False)

Forward_left=26
Backward_left=21
Forward_right = 16
Backward_right = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(Forward_left, GPIO.OUT)
GPIO.setup(Backward_left, GPIO.OUT)
GPIO.setup(Forward_right, GPIO.OUT)
GPIO.setup(Backward_right, GPIO.OUT)

def forward():
    GPIO.output(Forward_left, GPIO.HIGH)
    GPIO.output(Forward_right, GPIO.HIGH)  

def backward():
    GPIO.output(Backward_left, GPIO.HIGH)
    GPIO.output(Backward_right, GPIO.HIGH)

def turn_left():
    GPIO.output(Backward_left, GPIO.HIGH)
    GPIO.output(Forward_right, GPIO.HIGH)

def turn_right():
    GPIO.output(Forward_left, GPIO.HIGH)
    GPIO.output(Backward_right, GPIO.HIGH) 

def stop():
    GPIO.output(Forward_left, GPIO.LOW)
    GPIO.output(Forward_right, GPIO.LOW) 
    GPIO.output(Backward_left, GPIO.LOW)
    GPIO.output(Backward_right, GPIO.LOW)