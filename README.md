# PlayBot
* Streamer used: [mjpeg-streamer](https://github.com/jacksonliam/mjpg-streamer/tree/master/mjpg-streamer-experimental)
* Backend used: [Python Flask](http://flask.pocoo.org)

# Setup
1. Install MJPEG-Streamer and copy javascript-simple.html to www/ file (new file has responsive bootstrap code)
2. Setup MJPEG-Streamer to start on startup, in terminal:
```
sudo nano /etc/rc.local
```
Add the line:
```
mjpg_streamer -o "output_http.so -w /link/to/www" -i "input_raspicam.so -fps 15 -vf"
```
3. Edit Emailer.py and fill in email and password
4. Add entry to crontab so that web app will start on reboot after 30 seconds (to allow wifi to connect)
```
sudo crontab -e
```
Add the line:
```
@reboot sleep 30 && sudo python3 /home/pi/Desktop/web-server/app.py
```
5. Now when RPI is rebooted, you should recieve an email to the Pi's URL, and it will load web app and video stream
