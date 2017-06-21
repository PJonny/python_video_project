import cv2
import time
import filters
import numpy
from managers import WindowManager, CaptureManager

class Cameo(object):
    
    def __init__(self):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)
        self._captureManager = CaptureManager(
            cv2.VideoCapture(2), self._windowManager, False)
        self._curveFilter = filters.BGRPortraCurveFilter()
    
    def run(self):
        """Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:

            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            if frame is not None:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                hh, frame = cv2.threshold(frame.copy(), 127, 255, cv2.THRESH_BINARY)
                frame = cv2.Canny(frame, 100, 300)
                cv2.imshow("Gray", frame)
                # filters.strokeEdges(frame, frame)
                # self._curveFilter.apply(frame, frame)
                # TODO: Filter the frame (Chapter 3).
                pass
            self._captureManager.exitFrame()
            self._windowManager.processEvents()
    
    def onKeypress(self, keycode):
        """Handle a keypress.
        
        space  -> Take a screenshot.
        tab    -> Start/stop recording a screencast.
        escape -> Quit.
        
        """
        if keycode == 32: # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9: # tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo(
                    'screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

if __name__ == "__main__":
    Cameo().run()
