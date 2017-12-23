from flask import Flask, redirect
from flask_sockets import Sockets
from gpiozero import Robot
from gpiozero import Motor
from time import sleep

motor_left = Motor(12,16)
motor_right = Motor(20,21)

app = Flask(__name__)
sockets = Sockets(app)

def stop():
    motor_right.stop()
    motor_left.stop()

def forward(speed):
    motor_right.forward(speed)
    motor_left.forward(speed)

@app.route('/')
def index():
    return redirect("/static/index.html", code=302)

@app.route('/generate_204')
def captive_portal():
    return redirect("/static/index.html", code=302)

@app.route('/shutdown')
def shutdown():
    import os
    os.system("shutdown -h 0")
    quit()
    
@sockets.route('/socket')
def on_socket(ws):
    print('what')
    while not ws.closed:
        message = ws.receive()
        if message == 'S':
            stop()
        elif message == 'L':
            motor_right.forward()
            sleep(0.7)
            stop()
        elif message == 'R':
            motor_left.forward()
            sleep(0.7)
            stop()
        elif message == 'B':
            motor_right.backward(1)
            motor_left.backward(1)
        elif message == '1':
            forward(0.2)
        elif message == '2':
            forward(0.3)
        elif message == '3':
            forward(0.5)
        elif message == '4':
            forward(0.8)
        elif message == '5':
            forward(1)

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 80), app, handler_class=WebSocketHandler)
    server.serve_forever()
