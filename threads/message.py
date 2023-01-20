import threading

import socket
from datetime import datetime

import screens.message
from core import var


class Server(threading.Thread):
    def run(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(("0.0.0.0", 29718))
            sock.settimeout(0.5)
            sock.listen()
            while not var.quitting:
                try:
                    conn, addr = sock.accept()
                    with conn:
                        screens.message.sender = addr[0]
                        payload = ""
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                break
                            payload += data.decode()

                        screens.message.message = payload
                        var.cur_screen = screens.message.show
                        var.cur_handle = screens.message.handle
                        var.standby = False
                        var.last_active = datetime.now()
                except TimeoutError:
                    pass
