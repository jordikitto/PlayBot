import subprocess
import re

def get_ip_address():
    ip_address = subprocess.check_output(['hostname', '-I']).decode("utf-8")
    ip_pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    ip_address = re.findall(ip_pattern, ip_address)
    return str(ip_address[0])

def launch_streamer():
    # export LD_LIBRARY_PATH=/path/to/plugin/folder
    #path = "/home/pi/mjpg-streamer/mjpg-streamer-experimental"
    #subprocess.call(['export', 'LD_LIBRARY_PATH='+path])
    print(subprocess.check_output(['pwd']))

    #mjpg_streamer -o  -i 
    output_text = '"output_http.so -w /mjpg-streamer/www"'
    input_text = '"/mjpg-streamer/input_raspicam.so -fps 15 -vf"'
    streamer_args = ['./mjpg-streamer/mjpg_streamer', '-o', output_text, '-i', input_text]
    for arg in streamer_args:
        print(arg, end=" ")
    subprocess.call(streamer_args)