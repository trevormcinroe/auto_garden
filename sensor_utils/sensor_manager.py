"""

"""

import numpy as np
import pandas as pd


class SensorManager:

    def __init__(self,
                 camera):
        self.camera = camera

    def take_timelapse(self):
        """"""

        self.camera.take_timelapse()

    def take_video(self):
        """"""

        self.camera.take_video()