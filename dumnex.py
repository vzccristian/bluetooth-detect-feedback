# encoding=utf8
from gtts import gTTS
import time
import os
import yaml
import random
from bluetooth import *
import requests
import sys

userMac = "48:2C:A0:21:5D:39"
userId = "U1"
URL_BASE3 = 'https://dumnex-tratamiento.herokuapp.com/v1/valoracion?usuarioId='

if __name__ == '__main__':

    with open("feedback.yaml", 'r', encoding='utf8') as stream:
        try:
            feedback = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    name = list(feedback.keys())[0]

    print("Buscando {} bluetooth".format(userMac))
    while (1):
        check = 0
        print("Buscando dispositivos bluetooth...")
        nearby_devices = discover_devices(lookup_names=True)
        print("Encontrados {} dispositivos: ".format(len(nearby_devices)))
        print(nearby_devices)

        for dev in nearby_devices:
            check += 1
            if userMac == dev[0]:
                print("El usuario ha llegado.")
                try:
                    req = requests.get(URL_BASE3 + userId)
                    if req.status_code == 200:
                        try:
                            valoracion = int(req.text)
                            texto = feedback[name][valoracion][random.randint(0, len(feedback[name][valoracion])) - 1]

                            print("Valoración de hoy: {}. \n{}".format(valoracion, texto))

                            mytext = "Hola {}. {}".format(name, texto)

                            myobj = gTTS(text=mytext, lang="es", slow=False)
                            myobj.save("tempfile.mp3")

                            os.popen('mpg321 tempfile.mp3').read()
                            time.sleep(1)
                            os.system("rm -f tempfile.mp3")
                        except Exception:
                            pass
                except Exception:
                    pass
        time.sleep(2)
