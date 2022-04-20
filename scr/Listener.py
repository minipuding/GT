import pynput
import time
import PyQt5.QtCore as qc
import threading

class Listener(threading.Thread):
    CHOOSE_SIGNAL = qc.pyqtSignal()
    def __init__(self):
        threading.Thread.__init__(self)
        self.mouse_down = (0,0)
        self.mouse_up = (0,0)

    def on_click(self, x, y, button, pressed):
        if pressed == True:
            self.mouse_down = (x, y)
        else:
            self.mouse_up = (x, y)
            if self.mouse_down != self.mouse_up:
                ctrl = pynput.keyboard.Controller()
                with ctrl.pressed(pynput.keyboard.Key.ctrl):
                    ctrl.press('c')
                    ctrl.release('c')

    def run(self):
        with pynput.mouse.Listener(on_click=self.on_click) as mouse_listener:
            mouse_listener.join()