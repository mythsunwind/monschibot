<p align="center"><img src="./static/logo.svg" width="100" height="100" alt="Monschibot logo"></p>

# Monschibot

A remote controlled raspberry pi with a touch-enabled web interface that sends commands through websocket.

## Hardware

* Raspberry Pi3 Model B
* L298N dual motor controller
* Smart Robot Car Chassis Kit (included chassis, wheels, motors, battery box)
* Cheap portable power pack

Hardware assembled as described by Gautier Mechling on [Android Things](http://nilhcem.com/android-things/discovering-the-GPIO-api-building-a-remote-car)

## Remote control

The user connects securely to the Wifi access point called "Monschibot". On established connection the user gets redirected to a small website with control elements.

A python server serves the small website and listens to a websocket. The website uses javascript to send short commands (stop, left, right, speed) to the server. The server uses gpiozero library to control the motors accordingly.

## Setup

Install python libraries for the webserver:
```
apt-get install python3-gpiozero
apt-get install python3-flask
apt-get install python3-pip
pip3 install Flask-Sockets
```

Setup dnsmasq:
```
sudo service dnsmasq stop
sudo cp dnsmasq-monschibot /etc/dnsmasq.d/
```

Setup hostapd:
```
sudo cp hostapd.conf /etc/hostapd/
echo DAEMON_CONF="/etc/hostapd/hostapd.conf" >> /etc/default/hostapd
```

Setup wireless network interface:
```
sudo cp interfaces /etc/network/interfaces
```

Restart

## Start server

python monschibot.py

## License

All code is licensed under GNU GENERAL PUBLIC LICENSE Version 3.

Glyphs are licensed under [Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0) by [SmartIcons](https://github.com/frexy/glyph-iconset/).

The monschibot logo is licensed under [Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/).