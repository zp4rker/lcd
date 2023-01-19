import socket
from datetime import datetime

import screens.message
from core import var


def listen():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 29718))
        sock.settimeout(0.5)
        sock.listen()
        while not var.quitting:
            try:
                conn, addr = sock.accept()
                with conn:
                    text = f"Received message from {addr}:\n"

                    payload = ""
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        payload += data.decode()
                    text += payload

                    screens.message.message = text
                    var.cur_screen = screens.message.show
                    var.cur_handle = screens.message.handle
                    var.standby = False
                    var.last_active = datetime.now()
            except TimeoutError:
                pass
