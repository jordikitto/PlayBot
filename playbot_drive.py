#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 03:03:12 2019
PlayBot Drive/Launcher Functions
@author: emile
"""

#importing lib
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #set pin numbering to BCM system
GPIO.setwarnings(False)

#defining speeds in terms of duty cycles (can alter when testing)
low_speed = 40
med_speed = 70
high_speed = 100

#setting an initial speed
speed = high_speed

#initialise GPIO and  outputs

#left motor
GPIO.setup(26, GPIO.OUT)            #Assume initially this controls fwd motion
GPIO.setup(16, GPIO.OUT)            #Assume initially this controls bwd motion
pwm26 = GPIO.PWM(26, 100)			# 100Hz PWM Frequency is appropriate
pwm16 = GPIO.PWM(16, 100)	

#right motor
GPIO.setup(20, GPIO.OUT)            #Assume initially this controls fwd motion
GPIO.setup(21, GPIO.OUT)            #Assume initially this controls bwd motion
pwm20 = GPIO.PWM(20, 100)			# Initiate the PWM signal
pwm21 = GPIO.PWM(21, 100)			# Initiate the PWM signal

#launcher motor
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

#LEDS
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#Spares
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

# Functions ------------
    
def forward(): #when forward button is pressed
    #pwm26.start(speed)
    #pwm20.start(speed)
    GPIO.output(26, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)

    
def backward(): #when back button is pressed
    #pwm16.start(speed)
    #pwm21.start(speed)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    
def turn_right(): #for turning right while stationary
    #pwm20.start(speed)
    GPIO.output(20, GPIO.HIGH)

def turn_left(): #for turning left while stationary
    #pwm26.start(speed)
    GPIO.output(26, GPIO.HIGH)
    
def turn_fwd_left(): #for both forward and left being pressed
    pwm26.start(speed)
    pwm20.start(speed-20)
    
def turn_fwd_right(): #for both forward and right being pressed
    pwm26.start(speed-20)
    pwm20.start(speed)
    
def stop(): #when no button is being pressed
    #pwm26.stop()
    #pwm20.stop()
    #pwm16.stop()
    #pwm21.stop()
    GPIO.output(26, GPIO.LOW)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    
    
