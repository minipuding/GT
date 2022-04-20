import pynput
import time
import numpy as np
import pyperclip
import PyQt5
import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qg
import PyQt5.QtCore as qc
import sys
from threading import Thread

from MainWindow import Ui_GT
from google_trans_new import google_translator
import Listener

class GTWindow(qw.QMainWindow, Ui_GT):
    def __init__(self):
        super(GTWindow, self).__init__()
        self.setupUi(self)
        self.translator = google_translator()
        # self.mouse_listener = pynput.mouse.Listener(on_click=self.on_click)
        # self.mouse_listener.join()
        self.target_language = 'zh-cn'
        self.scr_text = 'Hello world!'
        self.tag_text = ''
        self.mouse_down = (0,0)
        self.mouse_up = (0,0)
        self.preclip = ''
        self.slot_translate()

        # Listener.CHOOSE_SIGNAL.connect(self.slot_translate)

    def slot_translate(self):
        while True:
            self.scr_text = pyperclip.paste()
            if self.scr_text == self.preclip:
                time.sleep(0.2)
            else:
                self.tag_text = self.translator.translate(self.scr_text, lang_tgt = self.target_language)
                self.text_browser.setText(self.tag_text)
                self.preclip = self.scr_text


def show_main_window():
    app = qw.QApplication(sys.argv)
    demo = GTWindow()
    demo.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    thread_1 = Thread(target=show_main_window)
    # thread_2 = Listener.Listener()
    # #
    thread_1.start()
    # thread_2.start()
    #
    thread_1.join()
    # thread_2.join()