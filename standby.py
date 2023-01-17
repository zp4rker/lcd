import time
from datetime import datetime

import main
import var


def watch():
    while not var.quitting:
        if not var.last_active:
            continue

        if (datetime.now() - var.last_active).total_seconds() < 30:
            continue

        main.disp.clear()
        var.standby = True
        time.sleep(30)
