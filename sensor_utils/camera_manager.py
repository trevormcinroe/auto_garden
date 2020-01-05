"""
A class for handling the camera module on a rapsberry pi.
CameraManager both takes pictures for a timelapse as well as videos.

It will create two folders within self.repo: timelapse, and video.
"""

import time
import os
import datetime
from picamera import PiCamera


class CameraManager:

    """
    Attributes:
        resolution (list or tuple): the w x h of the camera capture 
        num_picture (int): the number of pictures to include in the timelapse. Each picture will
                        be taken 1 second apart, so use this parameter to control the length of the
                        timelapse.
        video_length
        repo
    """

    def __init__(self, resolution, num_picture, video_length, repo):
        """"""

        self.camera = None
        self.resolution = resolution
        self.num_picture = num_picture
        self.video_length = video_length
        self.repo = repo
        self.hour = None

        self._initalize()

    def _initalize(self):
        """
        Handles initalization of the CameraManager class.
        Ensures proper folders for storage.
        Checks for the camera connections and starts it.
        """

        # Checking to see if the given repo folder can be found
        if not os.path.isdir(self.repo):
            raise FileNotFoundError('Cannot locate given repo.')

        # If they don't exist, create the two folders
        if 'timelapse' not in os.listdir(self.repo):
            os.mkdir(os.path.join(self.repo, 'timelapse'))
        if 'video' not in os.listdir(self.repo):
            os.mkdir(os.path.join(self.repo, 'video'))

        # Initalizing the camera connection
        self.camera = PiCamera()
        self.camera.resolution = self.resolution

    def _update_hour(self):
        """A simple method for updating the self.hour attribute"""
        day, hour = str(datetime.datetime.now()).split(' ')
        day = day.replace('-', '_')
        hour = hour.split('.')[0].replace(':', '')
        self.hour = day + "_" + hour
        del day, hour

        return self

    def take_timelapse(self):
        """
        The method that takes the timelapse. It works by taking self.num_pictures pictures,
        one every second. It then saves the images within the 'timelapse' folder within
        self.repo, using self.hour as the filename. After each picture, the class updates
        it's self.hour attribute to both stop file overwriting and to allow for sorting of the
        images into chronological order.
        """

        # Preliminaries of starting the camera, init the counter, and resetting the
        # self.hour attribute
        self.camera.start_preview()
        i = 0
        self._update_hour()

        while i < self.num_picture:
            self.camera.capture(os.path.join(self.repo, 'timelapse', f'{self.hour}.jpg'))
            time.sleep(1)
            i += 1
            self._update_hour()

    def take_video(self):
        """
        This method takes video. It works by using methods from the
        raspberry pi camera module. Simply takes footage of
        self.video_length seconds. The footage is saved within the
        self.repo/video folder. Files are names based on the self.hour
        attribute.
        """

        # Preliminaries of starting the camera, init the counter, and resetting the
        # self.hour attribute
        self.camera.start_preview()
        self._update_hour()

        # Starting the recording for self.video_length seconds
        self.camera.start_recording(os.path.join(self.repo, 'video', f'{self.hour}.jpg'))
        time.sleep(self.video_length)
        self.camera.stop_recording()
        self.camera.stop_preview()

