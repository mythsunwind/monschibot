# Monschibot

A remote controlled raspberry pi with a touch-enabled web interface that sends commands through websocket.

## Hardware

* Raspberry Pi3 Model B
* L298N dual motor controller
* Smart Robot Car Chassis Kit (included chassis, wheels, motors, battery box)
* Cheap portable power pack

Hardware assembled as described by Gautier Mechling: [Android Things](http://nilhcem.com/android-things/discovering-the-GPIO-api-building-a-remote-car)

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

## Start server

python monschibot.py
