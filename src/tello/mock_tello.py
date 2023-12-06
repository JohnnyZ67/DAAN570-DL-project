
class MockTello:

    def __init__(self):
        print("MOCK - CREATING TELLO OBJECT")

    def connect(self):
        print("MOCK - CONNECTING TO TELLO")

    def streamon(self):
        print("MOCK - TELLO VIDEO STREAMING ENABLED")
    
    def streamoff(self):
        print("MOCK - TELLO VIDEO STREAMING DISABLED")

    def get_frame_read(self):
        print("MOCK - CONNECTING TO TELLO")

    def end(self):
        print("MOCK - TELLO CONNECTION TERMINATED")

    def takeoff(self):
        print("MOCK - TELLO INITIATED AUTO TAKEOFF")
    
    def land(self):
        print("MOCK - TELLO INITIATED AUTO LANDING")
    
    def move_up(self, centimeters: int):
        print(f"MOCK - TELLO MOVING {centimeters} UP")
    
    def move_down(self, centimeters: int):
        print(f"MOCK - TELLO MOVING {centimeters} DOWN")

    def move_left(self, centimeters: int):
        print(f"MOCK - TELLO MOVING {centimeters} LEFT")

    def move_right(self, centimeters: int):
        print(f"MOCK - TELLO MOVING {centimeters} RIGHT")

    def move_forward(self, centimeters: int):
        print(f"MOCK - TELLO MOVING {centimeters} FORWARD")
    
    def move_back(self, centimeters: int):
        print(f"MOCK - TELLO MOVING {centimeters} BACK")

    def rotate_clockwise(self, degrees: int):
        print(f"MOCK - TELLO ROTATING {degrees} DEGREES CLOCKWISE")
    
    def rotate_counter_clockwise(self, degrees: int):
        print(f"MOCK - TELLO ROTATING {degrees} DEGREES COUNTER CLOCKWISE")