from tello.mock_tello import MockTello
from djitellopy import Tello
from keras.preprocessing.image import load_img, img_to_array
from skimage import transform
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import keras
import os

## Running controller in Dry run mode with following command
## DRYRUN=True python controller.py

class Controller:

    def __init__(self):
        self.model_selection = ""
        self.model = None
        self.classes = ["down", "ele", "palm", "palm_m", "palm_o", "palm_u", "pointer", "pointer_b", "pointer_f", "pointer_l", "pointer_r", "up"]
        self.drone_move_limit = 10 ## Distance in CM for Drone movements
        self.dry_run = os.getenv("DRYRUN", False)

        self.change_model("CNN")
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
            self.model_selection = "CNN"
            self.model = keras.models.load_model(f"{os.getcwd()}//models//hg_cnn_az_05.h5")
            print("Model changed to CNN")
        else:
            self.model_selection = "ViT"
            self.model = None
            print("Model changed to ViT")

    def get_evaluation(self, gesture_img_path):
        img = img_to_array(load_img(gesture_img_path, target_size = (224, 224)))
        # plt.imshow(img)
        # plt.show()
        input_arr = np.array([img])
        ## Returns our model's evaluation based on image
        
        if self.model_selection == "CNN":
            evaluation = self.model.predict(input_arr)
            max_index = np.argmax(evaluation, axis=-1)
            return self.classes[max_index[0]]

        return True
        
    def perform_move(self, gesture):
        if gesture == "pointer_f":
            self.tello.move_forward(self.drone_move_limit)
        elif gesture == "palm_m":
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