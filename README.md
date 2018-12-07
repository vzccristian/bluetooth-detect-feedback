# Detección de personas a través de dispositivo Bluetooth.

Proyecto de la asignatura de Desarrollo de Sistemas Hardware del Máster en Ingeniería Informática impartido por la UNEX. 
Este proyecto emplea una Raspberry Pi con acceso a bluetooth (ya sea nativo o mediante dongle USB compatible) para poder detectar personas en un entorno cercano mediante su dispositivo bluetooth asociado.

### Componentes principales.
- [Raspberry Pi](https://www.raspberrypi.org/)
- Bluetooth USB Dongle (Si fuera necesario)
- Salida imagen para visualización de información. 
- Salida audio a altavoces (o HDMI) 

### Dependencias
- [gTTS](https://pypi.org/project/gTTS/) Para retroalimentación por audio.
- [PyBluez](https://github.com/pybluez/pybluez) Para detección Bluetooth.
- [pyQt5](https://pypi.org/project/PyQt5/) Para retroalimentación por imagen.


### Funcionamiento

Antes de ejecutar la aplicación debemos de configurar el fichero "feedback.yaml" a nuestro gusto. Este fichero está formado en primer lugar por el nombre del usuario y a continuación por una serie de oraciones asociadas a un número comprendido entre 1 y 10.

El objetivo es informar a un usuario de su estado de salud, ya sea, para advertirlo de la necesidad de acudir al médico o para indicarle el buen estado de forma en el que se encuentra y otorgarle así de confianza en sí mismo.

La idea de este proyecto es dejar a un familiar que conozca bien al usuario rellenar a su gusto ese documento, sobretodo motivando al usuario cuando obtenga una puntuación alta (haciendo referencias a sus gustos y aficiones, o recordandole aspectos importantes para él.)

El fichero "feedback.yaml" acepta tantas frases por valoración como se deseen, es decir, podemos indicar por cada valor de 1 a 10 varias frases y el sistema tomará una de ellas en cada iteración. De esta forma, el sistema no resulta monótono para el usuario.

Ejemplo de fichero "feedback.yaml":

```yaml

---
Irene:
  1:
    - No ha sido tu mejor día. Visita a tu médico.
    - Es necesario que visites al médico.
  2:
    - No ha sido tu mejor día. Visita a tu médico.
    - Tienes que llamar al médico.
  3:
    - Podemos ir mejorando. Necesitas más actividad. ¿Qué tal un paseo?
    - Bueno, es cierto que podrías haberlo hecho mejor. Visita al médico.
  4:
    - Estás consiguiendo los objetivos. Sigue así. ¿Has dado ya un paseo?
  5:
    - Empiezas a estar en buena forma. Sigue así.
  6:
    - Hoy estás en muy buena forma. Sigue así.
    - Hoy has tenido buena actividad. Muy bien.
  7:
    - Hoy has estado fenomenal. Estás en plena forma. Sigue así.
    - Estás genial. Muy bien hecho.
  8:
    - Hoy debes de estar orgullosa. Has estado como una deportista.
    - Cada día estás mejor. Tienes una salud de hierro.
  9:
    - Increíble lo bien que te encuentras. Nuestros índices nos confirman que estás en PLENA FORMA. Sigue así.
    - Hoy has estado como una deportista de élite. Eres una crack. Sigue así.
  10:
    - Estás en mejor forma que Cristiano Ronaldo y Messi juntos. Sigue así.
    - Da gusto verte en este estado de forma. Tu salud está como un toro.
  
```

Una vez escrito el fichero a nuestro gusto, el equipo de DUMNEX se encargará de instalarlo en el dispositivo y configurarlo para que se ejecute de forma automática.

### Ejecución

Para ejecutar la aplicación:
```bash
python3 dumnexUi.py [FULL]
```

Indicandole cualquier argumento se desplegará en tamaño completo de pantalla. (OJO. Esto puede llevar después a no saber cerrar la aplicación.)

### Esquema de conexiones

![Esquema de conexiones](https://github.com/vzccristian/bluetooth-detect-feedback/esquema.png)
