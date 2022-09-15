**enable Network at Boot** 
`sudo raspi-config`
System Options->Network at Boot (enabled)

**added to /boot/config.txt**
```
#dtoverlay=vc4-fkms-v3d
dtoverlay=vc4-kms-v3d,noaudio=on
dtparam=audio=off
dtoverlay=hifiberry-dacplus
force_eeprom_read=0
gpu_mem=128
```
**print temperature alias**
`alias temp='vcgencmd measure_temp'`

***create desktop shortcut***

`cat /home/pi/Desktop/my-chromium.desktop`

```
[Desktop Entry]
Comment=Chromium
Terminal=false
Name=Chromium
Exec=/home/pi/salon-radio/start_chromium.sh
Type=Application
Icon=chromium-browser
```
'stop asking':
https://forums.raspberrypi.com/viewtopic.php?t=248380

***enable hardware accelaration in chrome***
chrome://flags:
Override software rendering list aka #ignore-gpu-blocklist;
GPU rasterization aka #enable-gpu-rasterization;
Zero-copy rasterizer aka #enable-zero-copy;
Enables Display Compositor to use a new gpu thread. aka #enable-drdc;
Out-of-process 2D canvas rasterization. aka #canvas-oop-rasterization.
then relaunched it using 
`chromium-browser --enable-features=VaapiVideoDecoder` command.

***install gpio listener***
`sudo pip3 install websockets`
add to /etc/rc.local
`/home/pi/salon-radio/start.sh &> /tmp/rc.local.log`

**install mopidy**
https://docs.mopidy.com/en/latest/installation/debian/#install-from-apt-mopidy-com
```
sudo adduser mopidy video
sudo adduser mopidy cdrom
```

https://mopidy.com/ext/
```
sudo python3 -m pip install Mopidy-TuneIn
sudo python3 -m pip install Mopidy-YouTube
sudo python3 -m pip install youtube-dl
sudo python3 -m pip install Mopidy-Iris
sudo python3 -m pip install Mopidy-Mobile
sudo python3 -m pip install Mopidy-SoundCloud
sudo python3 -m pip install Mopidy-ALSAMixer
sudo python3 -m pip install git+https://github.com/antosart/mopidy-cd
sudo python3 -m pip install Mopidy-Tidal
sudo apt-get install gstreamer1.0-plugins-bad
copy mopidy.conf to /etc/mopidy/
```
https://docs.mopidy.com/en/latest/running/service/

/etc/udev/rules.d/95-cd-devices.rules:
```
KERNEL=="sr0", SUBSYSTEM=="block", SUBSYSTEMS=="usb", ATTRS{idVendor}=="0e8d", ATTRS{idProduct}=="1887", TAG+="systemd", ENV{SYSTEMD_WANTS}="addcdtracks.service"
```
/etc/systemd/system/addcdtracks.service:
```
[Service]
Type=oneshot
ExecStart=python3.9 /home/pi/salon-radio/addcdtracks.py
```
**Kodi**

https://htpc.xyz/2020/10/22/kodi-instalacja-inputstream-adaptive-i-rtmp-input/

```
sudo apt-get install kodi-inputstream-adaptive
sudo apt-get install kodi-inputstream-rtmp
```
If plugins are installed turn them on:
Dodatki > Moje dodatki > Videoplayer InputStream
Check InputStream Adaptive and RTMP Input.

```
sudo pip install setuptools wheel pycryptodomex
wget https://github.com/castagnait/repository.castagnait/raw/kodi/repository.castagnait-2.0.0.zip
```
https://howtomediacenter.com/en/install-netflix-kodi-addon/
https://pimylifeup.com/raspberry-pi-netflix/

https://reviewvpn.com/install-hbo-max-kodi-addon/

copy api_keys.json:
```
{
    "keys": {
        "developer": {}, 
        "personal": {
            "api_key": "AIzaSyDakT9bp9z0BQoTA0TI7vpy3-iHcO_maUY", 
            "client_id": "885530799383-5g9q3b19lke77vr4lqjoouc40rtjieb8", 
            "client_secret": "U2KgBN0b3WE5fB_l4G1jHhFR"
        }
    }
}
```
to
/home/pi/.kodi/userdata/addon_data/plugin.video.youtube

**useful commands:**
```
sudo mopidyctl config
sudo systemctl start mopidy
sudo systemctl stop mopidy
sudo systemctl restart mopidy
sudo journalctl -u mopidy -f
sudo udevadm control --reload
sudo udevadm monitor

tail -f /var/log/syslog
tail -f -s 0 /var/log/kern.log

sudo tail -f /home/pi/.kodi/temp/kodi.log
```

**pir**
```sudo vi /boot/config.txt
sudo reboot
sudo vi /boot/config.txt
sudo reboot
lsmod | grep gpio
cat /proc/bus/input/devices
sudo apt-get install ir-keytable -y
ir-keytable
sudo ir-keytable -p all
sudo ir-keytable
ir-keytable -t -s rc0
```

**bluetooth**
https://forums.raspberrypi.com/viewtopic.php?t=235519
https://stackoverflow.com/questions/68728478/failed-to-set-power-on-org-bluez-error-blocked-problem

