import os
from tello.mock_tello import MockTello
from djitellopy import Tello

## Running controller in Dry run mode with following command
## DRYRUN=True python controller.py

class Controller:

    def __init__(self):
        self.dry_run = os.getenv("DRYRUN", False)
        if self.dry_run:
            print("MOCK - STARTING TELLO CONTROLLER")
            self.tello = MockTello()
        else:
            print("STARTING TELLO CONTROLLER")
            self.tello = Tello()

    def setup(self):
        ## Create model from saved weights
        self.model = True

    def get_evaluation(self):
        ## Returns our model's evaluation based on image
        return True
    

if __name__ == "__main__":
    controller = Controller()
    controller.main()