'''
Video service will use the display window values to create a window
and have functions to start, stop, and such
'''

import pyray as pr

class VideoService:
    def __init__(self, width, height, caption, fps):
        self._width = width
        self._height = height
        self._caption = caption
        self._fps = fps        

    def open_window(self):
        pr.init_window(self._width, self._height, self._caption)
        pr.set_target_fps(self._fps)

    def close_window(self):
        pr.close_window()

    def is_window_open(self):
        return not pr.window_should_close()
