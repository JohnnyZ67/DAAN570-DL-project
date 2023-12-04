from controller import Controller
from tkinter.font import Font
from PIL import ImageTk, Image
import tkinter as tk
import os
import random


class FlightControllerGUI(tk.Frame):
    
    def __init__(self, master):
        
        self.BASE_IMAGE_PATH = "D://Resources//DAAN_570_Archive//DAAN570_Data" # Change path to where your training and test data is

        tk.Frame.__init__(self, master)

        # self.board = Board(master)
        # self.board.pack(side=tk.LEFT, padx=1, pady=1)

        self.menu = tk.Frame(self)
        self.selected_model = tk.StringVar(self.menu, "CNN")

        tk.Label(self.menu, text="Select the Deep Learning Model you would like to use.", font=Font(size=20)).pack(
            padx=3, pady=3)

        ## Model Selection
        self.model_selector_box = tk.Frame(self.menu)

        self.cnn_button = tk.Radiobutton(self.model_selector_box, text="CNN Model", variable=self.selected_model, value="CNN", font=Font(size=18))
        self.cnn_button.pack(padx=3, pady=1)

        self.vit_button = tk.Radiobutton(self.model_selector_box, text="ViT Model", variable=self.selected_model, value="ViT", font=Font(size=18))
        self.vit_button.pack(padx=3, pady=1)

        self.model_selector_box.pack(fill=tk.X, padx=1, pady=1)
        
        ## Displays current gesture:
        self.current_img = Image.open(f"{self.BASE_IMAGE_PATH}//palm_o//sub00_palm_o_0006.png")
        self.tk_img = ImageTk.PhotoImage(self.current_img)
        self.gesture_label = tk.Label(self.menu, text="Gesture:")
        self.gesture_label.pack(fill=tk.X, padx=1, pady=1)

        self.img_label = tk.Label(self.menu, image=self.tk_img)
        self.img_label.pack(fill=tk.X, padx=1, pady=1)

        ## Gesture Buttons:
        self.down_btn = tk.Button(self.menu, text="DOWN - Fly Down 10cm", command=lambda: self.select_gesture("down"), font=Font(size=14))
        self.down_btn.pack(fill=tk.X, padx=1, pady=1)

        self.up_btn = tk.Button(self.menu, text="UP - Fly Up 10cm", command=lambda: self.select_gesture("up"), font=Font(size=14))
        self.up_btn.pack(fill=tk.X, padx=1, pady=1)

        self.left_btn = tk.Button(self.menu, text="LEFT - Fly Left 10cm", command=lambda: self.select_gesture("pointer_l"), font=Font(size=14))
        self.left_btn.pack(fill=tk.X, padx=1, pady=1)

        self.right_btn = tk.Button(self.menu, text="RIGHT - Fly Right 10cm", command=lambda: self.select_gesture("pointer_r"), font=Font(size=14))
        self.right_btn.pack(fill=tk.X, padx=1, pady=1)

        self.frwd_btn = tk.Button(self.menu, text="FORWARD - Fly Forward 10cm", command=lambda: self.select_gesture("pointer_f"), font=Font(size=14))
        self.frwd_btn.pack(fill=tk.X, padx=1, pady=1)

        self.back_btn = tk.Button(self.menu, text="BACK - Fly Backwards 10cm", command=lambda: self.select_gesture("pointer_b"), font=Font(size=14))
        self.back_btn.pack(fill=tk.X, padx=1, pady=1)

        self.open_btn = tk.Button(self.menu, text="OPEN - Start and Liftoff", command=lambda: self.select_gesture("palm_o"), font=Font(size=14))
        self.open_btn.pack(fill=tk.X, padx=1, pady=1)

        self.land_btn = tk.Button(self.menu, text="L - Land the drone", command=lambda: self.select_gesture("ele"), font=Font(size=14))
        self.land_btn.pack(fill=tk.X, padx=1, pady=1)

        self.menu.pack()  

        self.flight_controller = Controller()
        self.flight_controller.main()

    def _update_image(self, gesture):
        random_image = random.choice(os.listdir(f"{self.BASE_IMAGE_PATH}//{gesture}"))
        self.current_img = Image.open(f"{self.BASE_IMAGE_PATH}//{gesture}//{random_image}")
        self.tk_img = ImageTk.PhotoImage(self.current_img)

        self.img_label.destroy()
        self.img_label = tk.Label(self.menu, image=self.tk_img)
        self.img_label.pack(fill=tk.X, after=self.gesture_label, before=self.down_btn, padx=1, pady=1)

    def select_gesture(self, gesture):
        self._update_image(gesture)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tello Gesture Flight Controller")
    FlightControllerGUI(root).pack()
    root.resizable(height=True, width=True)
    root.mainloop()
