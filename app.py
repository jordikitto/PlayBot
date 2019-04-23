import RPi.GPIO as GPIO
from send_email import Emailer
from pi_command import get_ip_address
from flask import Flask, render_template, request
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

if __name__ == "__main__":
   # Email IP address
   print("Mailing IP")
   mail = Emailer()
   mail.send_ip()
   # Start web app
   app.run(host=ip_address, port=80, debug=False, threaded=True)
