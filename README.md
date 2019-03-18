# RPi_RGB_led_strrip_screen
building a screen of RGB led strips [WS2812b] & [WS2801] , displaying Images and maybe videos

# primary system packages [not proved to be needed]
    1- Terminal     : " sudo apt-get update "
    2- Terminal     : " sudo apt-get install gcc make build-essential python3-dev git scons swig "

# disable audio output  [not proved to be needed]
    1.1- Terminal     : " sudo nano /etc/modprobe.d/snd-blacklist.conf "
    1.2- Add line     : " blacklist snd_bcm2835 "
    1.3- Save changes : {CTRL + O} then {ENTER} then {CTRL + X}

    2.1- Terminal     : " sudo nano /boot/config.txt "
    2.2- find line    : " dtparam=audio=on "
    2.3- comment it   : " #dtparam=audio=on "

    3  - Terminal     : " sudo reboot "

# needed python libraries
1- pillow library, used for image handling:
> sudo pip3 install pillow

2- rpi_ws281x library, used for handling LEDs [WS2812b] :
> sudo pip3 install rpi_ws281x

3- library for [WS2801] :
> sudo pip3 install adafruit-ws2801

# display images
    1- go to the project folder.
    2- Terminal : " sudo python3 main.py -i <path/to/image>"
    3- Example  : " sudo python3 main.py -i test/red.jpg "
