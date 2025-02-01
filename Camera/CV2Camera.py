from Camera.ICamera import ICamera
import cv2
import numpy as np

class CV2Camera(ICamera):
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def get_frame(self) -> np.ndarray:
        ret, frame = self.camera.read()
        return frame