#!/usr/bin/python3

import RPi.GPIO as GPIO
from send_email import Emailer
from pi_command import get_ip_address
from flask import Flask, render_template, request
import playbot_drive as drive
app = Flask(__name__)

GPIO.setmode(GPIO.BCM) # Use BCM Mode

ip_address = get_ip_address()

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   23 : {'name' : 'GPIO 23', 'state' : GPIO.LOW}}

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   ip_address = get_ip_address()
   return render_template('main.html', **templateData, ip=ip_address)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/ledAction")
def action():
   # Convert the pin from the URL into an integer:
   changePin = int(request.args.get("changePin", 0))
   # Get the action
   action = request.args.get("action", 0)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)

# Send the robot forward
@app.route("/forward")
def forward():
   drive.forward()
   return render_template('main.html')

# Send the robot backward
@app.route("/backward")
def backward():
   drive.backward()
   return render_template('main.html')

# Send the robot turn_right
@app.route("/turn_right")
def turn_right():
   drive.turn_right()
   return render_template('main.html')

# Send the robot turn_left
@app.route("/turn_left")
def turn_left():
   drive.turn_left()
   return render_template('main.html')

# Send the robot stop
@app.route("/stop")
def stop():
   drive.stop()
   return render_template('main.html')

# Set speed to fast
@app.route("/speed_fast")
def speed_fast():
   drive.set_speed_fast()
   return render_template('main.html')

# Set speed to med
@app.route("/speed_med")
def speed_med():
   drive.set_speed_med()
   return render_template('main.html')

# Set speed to slow
@app.route("/speed_slow")
def speed_slow():
   drive.set_speed_slow()
   return render_template('main.html')

if __name__ == "__main__":
   # Email IP address
   print("Mailing IP")
   mail = Emailer()
   mail.send_ip()
   # Start web app
   app.run(host=ip_address, port=80, debug=True, threaded=True)
