import socket
import time

def server(app, port=14009):
    BIND_IP = "127.0.0.1"
    UDP_PORT = port

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((BIND_IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        app.set_var('last_received', time.time())
        array = data.decode('utf-8').split(',')
        g = int(float(array[0])*10)
        # aoa = int(math.degrees(float(array[1]))*10)
        aoa = int(float(array[1])*10)
        gear_mute = int(array[2])
        if not app.get_var('audio_testing'):
            app.set_var('g', g)
            app.set_var('aoa', aoa)
            app.set_var('gear_mute', gear_mute)
            app.indicators_frame.g_indicator.update()
            app.indicators_frame.aoa_indicator.update()
