import leap
from typing import Optional
from leap.events import Event
from leap.enums import EventType
from leap.exceptions import LeapError

class GestureListener(leap.Listener):

    def __init__(self, target: EventType):
        self._target = target
        self.event: Optional[Event] = None

    def on_connection_event(self, event):
        print("CONNECTED")

    def on_device_event(self, event):
        try:
            with event.device.open():
                info = event.device.get_info()
        except leap.LeapCannotOpenDeviceError:
            info = event.device.get_info()

        print(f"Found device {info.serial}")

    def on_error(self, error):
        print(error)