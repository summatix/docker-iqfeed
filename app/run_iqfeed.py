#!/usr/bin/env python3

"""
Continuously monitors for iqfeedclient responsiveness. Initiates the
application if it's not already running.
"""

import os
import subprocess
import sys
import time

import pyiqfeed.service


if __name__ == "__main__":
    while True:
        time.sleep(5)

        if not pyiqfeed.service._is_iqfeed_running():
            print("iqfeedclient is not running")

            subprocess.Popen((
                "/usr/bin/wine", "iqconnect.exe",
                "-product", sys.argv[1],
                "-version", "CONTAINER",
                "-login", sys.argv[2],
                "-password", sys.argv[3],
                "-autoconnect", "-savelogininfo"
            ))

        else:
            print("iqfeedclient is running")
