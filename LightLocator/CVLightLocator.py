from LightLocator.ILightLocator import ILightLocator
from typing import List, Tuple
import cv2
import numpy as np
import imutils

class CVLightLocator(ILightLocator):
    def __init__(self, config):
        self.config = config

    def locate_sources(self, frame: np.ndarray) -> List[Tuple[int, int]]:
        """
        Github Copiliot generated CV code
        """
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Apply a Gaussian blur to the frame
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)
        # Apply a threshold to the frame
        thresh = cv2.threshold(blurred, self.config['threshold'], 255, cv2.THRESH_BINARY)[1]
        # Perform a series of erosions and dilations to remove small blobs
        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=4)
        # Find contours in the thresholded frame
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        # Initialize the list of light sources
        lights = []
        # Loop over the contours
        for c in cnts:
            # Compute the center of the contour
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # Add the center to the list of light sources
            lights.append((cX, cY))
        return lights