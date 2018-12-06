# encoding=utf8
from gtts import gTTS
import time
import os
import yaml
import random
from bluetooth import *
import requests
import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
import threading

userMac = "bc:6e:64:1f:0a:8d"
userId = "U1"
URL_BASE3 = 'https://dumnex-tratamiento.herokuapp.com/v1/valoracion?usuarioId='


class Communicate(QtCore.QObject):
    myGUI_signal = QtCore.pyqtSignal(int, str)


class Display(QMainWindow):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("display.ui", self)
        self.setWindowTitle("DUMNEX")
        self.texto.setWordWrap(True)
        try:
            self.t = threading.Thread(name='qtThread', target=qtThread, args=(self.setFeedback,))
            self.t.start()
        except (KeyboardInterrupt, SystemExit):
            self.t._stop()

    def setFeedback(self, valoracion, texto):
        print("V:{} T:{}".format(valoracion, texto))
        try:
            if valoracion > 0:
                self.valoracion.setText(str(valoracion))
            else:
                self.valoracion.setText("")
        except Exception:
            print("Exception.")
            self.valoracion.setText("")
        try:
            self.texto.setText(texto)
        except Exception:
            print("Exception.")
            self.texto.setText("")

    def kill(self):
        self.t.do_run = False


def qtThread(callback):
    mysrc = Communicate()
    mysrc.myGUI_signal.connect(callback)
    t = threading.currentThread()
    encontrado = False
    with open("feedback.yaml", 'r', encoding='utf8') as stream:
        try:
            feedback = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    name = list(feedback.keys())[0]
    mysrc.myGUI_signal.emit(-1, "Esperando por "+name)  # Emit
    print("Buscando dispositivo: {}".format(userMac.upper()))

    while getattr(t, "do_run", True):
        # Main Code

        check = 0
        print("Buscando dispositivos bluetooth...")
        nearby_devices = discover_devices(lookup_names=True)
        print("Encontrados {} dispositivos: ".format(len(nearby_devices)))
        print(nearby_devices)

        for dev in nearby_devices:
            check += 1
            if userMac.upper() == dev[0].upper():
                print("El usuario ha llegado.")
                if not encontrado:
                    encontrado = True
                    try:
                        req = requests.get(URL_BASE3 + userId)
                        if req.status_code == 200:
                            try:
                                valoracion = int(req.text)
                                texto = feedback[name][valoracion][random.randint(0, len(feedback[name][valoracion])) - 1]
                                print("Valoración de hoy: {}. \n{}".format(valoracion, texto))
                                mytext = "Hola {}. {}".format(name, texto)

                                mysrc.myGUI_signal.emit(valoracion, mytext)  # Emit

                                myobj = gTTS(text=mytext, lang="es", slow=False)
                                myobj.save("tempfile.mp3")

                                os.popen('mpg321 tempfile.mp3').read()
                                time.sleep(1)
                                os.system("rm -f tempfile.mp3")
                            except Exception:
                                pass
                    except Exception:
                        pass
            elif (len(nearby_devices) == check):
                encontrado = False
		check = 0
                mysrc.myGUI_signal.emit(-1, "Esperando por "+name)  # Emit
        if len(nearby_devices) == 0:
            encontrado = False
            mysrc.myGUI_signal.emit(-1, "Esperando por "+name)  # Emit

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
