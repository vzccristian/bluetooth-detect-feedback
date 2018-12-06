from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import sys
import threading
import time
import os

class Communicate(QtCore.QObject):
    myGUI_signal = QtCore.pyqtSignal(int, str)

class Display(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("display.ui", self)
        self.setWindowTitle("DUMNEX")
        try:
            self.t = threading.Thread(name='qtThread', target=qtThread, args=(self.setFeedback,))
            self.t.start()
        except (KeyboardInterrupt, SystemExit):
            self.t._stop()

    def setFeedback(self, valoracion, texto):
        print(valoracion, texto)

    def kill(self):
        self.t.do_run = False


def qtThread(callback):
    mysrc = Communicate()
    mysrc.myGUI_signal.connect(callback)
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        # Do something useful here.
        msgForGui = 'This is a message to send to the GUI'
        mysrc.myGUI_signal.emit(10,"hola")
        time.sleep(2)
        # So now the 'callbackFunc' is called, and is fed with 'msgForGui'
        # as parameter. That is what you want. You just sent a message to
        # your GUI application! - Note: I suppose here that 'callbackFunc'
        # is one of the functions in your GUI.
        # This procedure is thread safe.
    sys.exit(0)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        mainWindow = Display()
        mainWindow.showMaximized()
        # mainWindow.showFullScreen()
        app.exec_()
        mainWindow.kill()
    except (KeyboardInterrupt, SystemExit):
        mainWindow.kill()
        sys.exit(0)
