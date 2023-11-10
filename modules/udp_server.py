import socket
import time

def server(app, port=14009):
    BIND_IP = "127.0.0.1"
    UDP_PORT = port

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((BIND_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        array = data.decode('utf-8').split(',')
        g = int(float(array[0])*10)
        aoa = int(float(array[1])*10)
        app.set_var('g', g)
        app.set_var('aoa', aoa)
        app.indicators_frame.g_indicator.update()
        app.indicators_frame.aoa_indicator.update()
