import cv2
import numpy as np
from Camera.ICamera import ICamera

class CV2Camera(ICamera):
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def get_frame(self) -> np.ndarray:
        ret, frame = self.camera.read()
        return frame