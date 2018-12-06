from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import sys
import threading

class Display(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("display.ui", self)
        self.setWindowTitle("DUMNEX")
        myThread()
        # t = threading.Thread(name='myThread', target=myThread, args=())
        # t.start()

class myThread():
    def __init__(self):
        while(1):
            print("Hola")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Display()
    mainWindow.show()
    sys.exit(app.exec_())
