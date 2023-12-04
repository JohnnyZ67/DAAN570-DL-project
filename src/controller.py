import os
import numpy as np
from tello.mock_tello import MockTello
from djitellopy import Tello

## Running controller in Dry run mode with following command
## DRYRUN=True python controller.py

class Controller:

    def __init__(self):
        self.dry_run = os.getenv("DRYRUN", False)

    def main(self):

        if self.dry_run:
            print("MOCK - STARTING TELLO CONTROLLER")
            tello = MockTello()
        else:
            print("STARTING TELLO CONTROLLER")
            tello = Tello()