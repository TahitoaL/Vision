#Cameo.py

import cv2
from CaptureManager import CaptureManager
from WindowManager import WindowManager

class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
