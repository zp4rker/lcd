import time
from datetime import datetime

import var


def watch(display):
    while not var.quitting:
        if not var.last_active:
            continue

        if (datetime.now() - var.last_active).total_seconds() < 30:
            continue

        display.clear()
        var.standby = True
        time.sleep(30)
