# PlayBot
This project is an implementation for a web app controlled robot. It only works over local wifi but allows the user to connect to the robot and control is on any browser capable device that they please. It has the following features

* Auto hotspot creation on power on with captive portal for user to enter their own wifi details for connect and email details for recieving an email with IP address of robot (for connecting)
* Automatic emailing of local IP for easy connection of local WiFi
* Responsive web app interface for driving robot, setting robot speed, and activating robot launcher
* Various failsafes for handling setup process for user (first dot point) and control of robot (but of course, these failsafes can be expanded and improved in future versions)

The result of this project is entirely the work of myself, with credits to the following resources and key tutorials:
* Operating System: Raspberry Pi [Raspbian](https://www.raspberrypi.org/downloads/)
* Camera Streamer used: [mjpeg-streamer](https://github.com/jacksonliam/mjpg-streamer/tree/master/mjpg-streamer-experimental)
* Control Web Backend used: [Python Flask](http://flask.pocoo.org)
* Setup Backend used: [Nginx](https://www.nginx.com) and [PHP](https://www.php.net)
* Front End UI: [Bootstrap](https://getbootstrap.com) and [jQuery](https://jquery.com)
* Initial Auto Hotspot Script: [Raspberry Pi - Auto WiFi Hotspot Switch - Direct Connection](http://www.raspberryconnect.com/network/item/331-raspberry-pi-auto-wifi-hotspot-switch-no-internet-routing)
* Initial Captive Portal Implementation: [Setting up a Raspberry Pi Captive Portal](https://pimylifeup.com/raspberry-pi-captive-portal/)

(*Note: Unfortunately I'm writing this setup after development has finished, so the setup hasn't been tested from scratch, and is vague at times*)
# Setup Control Web App
1. Install MJPEG-Streamer and copy javascript-simple.html from misc/ to www/ file (new file has responsive bootstrap code)
2. Setup MJPEG-Streamer to start on startup, in terminal:
```
sudo nano /etc/rc.local
```
Add the line (replace /link/to/www):
```
mjpg_streamer -o "output_http.so -w /link/to/www" -i "input_raspicam.so -fps 15 -vf"
```
You can edit ```-fps``` and change ```-vf``` to ```-hf``` if you prefer horizontal flip, or remove for no flip.
3. Add service to start Python Flask server. Service can be found in `hotspot/config/flask-server.service`, you'll need to update the path to the `app.py` file. Copy the updated file into your services folder so it works with `systemctl`.
# Setup Autohotspot Functionality
1. Basically, follow the tutorials [Raspberry Pi - Auto WiFi Hotspot Switch - Direct Connection](http://www.raspberryconnect.com/network/item/331-raspberry-pi-auto-wifi-hotspot-switch-no-internet-routing) and [Setting up a Raspberry Pi Captive Portal](https://pimylifeup.com/raspberry-pi-captive-portal/), but replace the files they mention with the files from `hotspot/config`.
2. Copy `hotspot/config/autohotspot.service` into services folder so it works with `systemctl`.
3. Enable `Autohotspot.service` to run on startup. 

*File paths should be full, e.g. /home/pi/Desktop/PlayBot*

# Usage
At this point, if setup is successful, it should operate as follows.
1. On power up, the robot will not know any wifi networks of have email details. `autohotspot.service` will trigger at startup, realise this, and create a hotspot for the user to connect to and fill in these details. It should take about 30 seconds for hotspot to appear after startup
2. User can then connect to wifi SSID `PlayBot`, where a captive portal will present asking for email details first, then wifi details. 
3. Upon successful submission of details, hotspot will shutdown and regular WiFi will boot up and connect to input WiFi details, then send user an email with details for how to connect to and control robot.
4. User can open email, click link and be taken to web app, where they see a video feed from the camera and controls to drive the robot and shoot the launcher.
