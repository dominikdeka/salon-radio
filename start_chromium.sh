if [ $# -eq 0 ]
then
  python3.9 /home/pi/salon-radio/start_chromium.py;
  chromium-browser --enable-features=VaapiVideoDecoder;
else
  python3.9 /home/pi/salon-radio/start_chromium.py;
  chromium-browser $1 --enable-features=VaapiVideoDecoder;
fi
