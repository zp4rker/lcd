import time
from datetime import datetime

import var


def watch():
    if not var.last_active:
        var.last_active = datetime.now()

    while not var.quitting:
        if not var.last_active:
            continue

        if (datetime.now() - var.last_active).total_seconds() < 15:
            continue

        if not var.standby:
            var.standby = True
            var.display.clear()
            time.sleep(15)
