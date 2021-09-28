#CaptureManger.py

import cv2
import numpy as np
import time

class CaptureManager(object):

    def __init__(self, capture, previewWindowManager = None, shouldMirrorPreview = False) -> None:
        
        self.previewWindowManager = previewWindowManager
        self.shouldMirrorPreview = shouldMirrorPreview

        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None

        self._startTime = None
        self._framesElapsed = long(0)
        self._fpsEstimated = None