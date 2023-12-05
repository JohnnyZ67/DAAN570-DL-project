from tello.mock_tello import MockTello
from djitellopy import Tello
import keras
import os

## Running controller in Dry run mode with following command
## DRYRUN=True python controller.py

class Controller:

    def __init__(self):
        self.model = ""
        self.change_model("CNN")
        self.drone_move_limit = 10 ## Distance in CM for Drone movements
        self.dry_run = os.getenv("DRYRUN", False)
        if self.dry_run:
            print("MOCK - STARTING TELLO CONTROLLER")
            self.tello = MockTello()
        else:
            print("STARTING TELLO CONTROLLER")
            self.tello = Tello()
        
    def setup(self):
        self.tello.connect()
        self.tello.takeoff()
    
    def disconnect(self):
        self.tello.land()
        self.tello.end()

    def change_model(self, model):
        if model == self.model:
            print("No model change required")
        elif model == "CNN":
            self.model = keras.models.load_model(f"{os.getcwd()}//models//hg_cnn_az_07.keras")
            print("Model changed to CNN")
        else:
            self.model = "ViT"
            print("Model changed to ViT")

    def get_evaluation(self, gesture_img):
        ## Returns our model's evaluation based on image
        return True
    
    def perform_move(self, gesture):
        if gesture == "pointer_f":
            self.tello.move_forward(self.drone_move_limit)
        elif gesture == "pointer_b":
            self.tello.move_back(self.drone_move_limit)
        elif gesture == "pointer_l":
            self.tello.move_left(self.drone_move_limit)
        elif gesture == "pointer_r":
            self.tello.move_right(self.drone_move_limit)
        elif gesture == "palm":
            self.tello.rotate_clockwise(self.drone_move_limit)
        elif gesture == "palm_u":
            self.tello.rotate_counter_clockwise(self.drone_move_limit)
        elif gesture == "up":
            self.tello.move_up(self.drone_move_limit)
        elif gesture == "down":
            self.tello.move_down(self.drone_move_limit)
        else:
            print(f"{gesture} is not a recognized gesture. No action being made")
    

if __name__ == "__main__":
    controller = Controller()
    controller.main()