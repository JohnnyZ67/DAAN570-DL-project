import leap
import time
import os
import cv2
import ctypes
import numpy as np
from cffi import FFI
from custom_leap.gesture_listener import GestureListener
from leap.events import ImageEvent
from leap.event_listener import LatestEventListener
from leap.datatypes import FrameData
from leap.enums import PolicyFlag
from tello.mock_tello import MockTello
from djitellopy import Tello

## Running controller in Dry run mode with following command
## DRYRUN=True python controller.py

class Controller:

    def __init__(self):
        self.dry_run = os.getenv("DRYRUN", False)

    def main(self):
        ffi = FFI()

        if self.dry_run:
            print("MOCK - STARTING TELLO CONTROLLER")
            tello = MockTello()
        else:
            print("STARTING TELLO CONTROLLER")
            tello = Tello()

        gesture_listener = LatestEventListener(leap.EventType.Image)
        connection = leap.Connection()
        connection.add_listener(gesture_listener)

        with connection.open() as connection:
            connection.set_policy_flags(flags_to_set=[PolicyFlag.Images])

            while True:
                time.sleep(1)
                event = gesture_listener.event
                if event is None:
                    continue

                image_l = event.image[0]
                image_r = event.image[1]

                print(image_l.matrix_version)
                print(image_r.matrix_version)
                print(image_l.c_data.data)
                buffer = ffi.buffer(cdata=image_l.c_data.data, size=153600)
                print(cv2.imdecode(np.asarray(buffer[:]), cv2.IMREAD_COLOR))
                print(image_l.c_data.offset)
                print(image_l.c_data.properties.width)
                print(image_l.c_data.properties.height)

                # cv2.imshow("frame", np.ctypeslib.as_array(image_l.c_data.data))

                break



if __name__ == "__main__":
    controller = Controller()
    controller.main()