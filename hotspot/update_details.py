#!/usr/bin/python3

import csv
import os
import subprocess

entry_wifi = '''ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
country=AU
network={{
    ssid="{0}"
    psk="{1}"
    key_mgmt=WPA-PSK
}}\n\n'''

entry_wifi_uni = '''ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
country=AU
network={{
    ssid="{0}"
    scan_ssid=1
    key_mgmt=WPA-EAP
    group=CCMP TKIP
    eap=PEAP
    identity="{1}"
    password="{2}"
    phase1="peapver=0"
    phase2="MSCHAPV2"
}}\n\n'''

# Read WPA supplicant
with open('/etc/wpa_supplicant/wpa_supplicant.conf','a') as wpa_file:
    # Read wifi details
    with open("wifi_details.txt") as wifi_file:
        csv_wifi = csv.reader(wifi_file)
        for details in csv_wifi:
            ssid = details[0]
            is_uni = bool(details[1])
            username = details[2]
            password = details[3]

            # Skip malformed entries
            if (ssid == "" or password == ""):
                continue

            if (not is_uni):
                wpa_entry = entry_wifi.format(ssid, password)
                wpa_file.write(wpa_entry)
            else:
                # Skip malformed entries
                if (username == ""):
                    continue

                wpa_entry = entry_wifi_uni.format(ssid, username, password)
                wpa_file.write(wpa_entry)

# Delete WIFI details file after we've read it
os.remove("wifi_details.txt")

# Call autohotspot now that we have new wifi details
subprocess.call(["sudo", "systemctl", "restart", "autohotspot.service"])
