# encoding=utf8
from gtts import gTTS
import time
import os
import yaml
import random
import pprint
from bluetooth import *
import requests

userMac="38:37:8B:C6:80:CB"
userId="U1"
URL_BASE3 = 'https://dumnex-tratamiento.herokuapp.com/v1/valoracion?usuarioId='

with open("feedback.yaml", 'r', encoding='utf8') as stream:
    try:
        feedback = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

while(1):
    print("Buscando dispositivos bluetooth...")
    nearby_devices = discover_devices(lookup_names = True)
    print("Encontrados {} dispositivos: ".format(len(nearby_devices)))
    print(nearby_devices)
    for dev in nearby_devices:
        if (userMac == dev[0]):
            print("El usuario ha llegado.")
            name = list(feedback.keys())[0]
            req = requests.get(URL_BASE3+userId)
            if (req.status_code == 200):
                try:
                    valoracion = int(req.text)
                    texto = feedback[name][valoracion][random.randint(0, len(feedback[name][valoracion]))-1]
                    print("Valoración de hoy: {}. \n{}".format(valoracion,texto))
                    mytext = "Hola {}. {}".format(name, texto)
                    myobj = gTTS(text=mytext, lang="es", slow=False)
                    myobj.save("tempfile.mp3")
                    os.popen('mpg321 tempfile.mp3').read()
                    # os.system("mpg321 tempfile.mp3")
                    time.sleep(1)
                    os.system("rm -f tempfile.mp3")
                except Exception:
                    pass
    time.sleep(2)
