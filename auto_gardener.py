"""

"""

from sensor_utils.sensor_manager import SensorManager
from file_utils.file_manager import FileManager
import time


class AutoGardener:

    def __init__(self,
                 file_manager,
                 sensor_manager,
                 image_mode):
        self.file_manager = file_manager
        self.sensor_manager = sensor_manager
        self.image_mode = image_mode

        self._register()

    def _register(self):
        """"""

        if self.image_mode not in ['hourly', 'else']:
            raise AttributeError('Given image_mode not supported.')

    def _set_image_mode(self, mode):
        """

        Modes:
            hourly: alternates between taking pictures and videos every hour

        Args:
            mode:

        Returns:

        """

        # Setting the self.mode attribute
        self.mode = mode

        # Now we need to update the attributes of the CameraManager
        # that is held within the SensorManager
        if mode == 'hourly':
            self.sensor_manager.camera.num_picture = 3600
            self.sensor_manager.camera.video_length = 3600

        return self

    def run_camera(self):
        """"""

        # Since the self._set_image_mode() method takes care of the atrributes
        # of the SensorManager's CameraManager, all we need to do is run, in a loop
        # the two methods:
        while True:
            self.sensor_manager.take_timelapse()
            self.sensor_manager.take_video()


