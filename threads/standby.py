import threading
import time
from datetime import datetime

from core import var


class WatchDog(threading.Thread):
    started = False

    def run(self) -> None:
        self.started = True

        if not var.last_active:
            var.last_active = datetime.now()

        while not var.quitting:
            if not var.last_active:
                continue

            if (datetime.now() - var.last_active).total_seconds() < 15:
                continue

            if not var.standby:
                var.standby = True
                var.display.command(0x10)
                time.sleep(15)
