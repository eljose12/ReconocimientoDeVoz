import numpy as np
import time
import tensorflow as tf
from tensorflow import keras

from keras import models

from recording import record_audio, terminate
from procesador import preprocess_audiobuffer

import pyttsx3

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

commands = ['no', 'gracias', 'estacion', 'cuanto', 'servicio', 'cine', 'sansimon',
'heladeria', 'rebaja', 'bien', 'plaza', 'adios', 'pare', 'mercado', 'hola']


loaded_model = models.load_model("saved_model")

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    
    confidence = tf.nn.softmax(prediction)
    max_confidence = np.max(confidence)

    resultado = [command, max_confidence] 

    return resultado

def escuchar_comando():
    presicion = 0
    while presicion < 0.85:
        print("listo?")
        time.sleep(2)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Habla")
        res = predict_mic()
        comando = res[0]
        presicion = res[1]
        print(comando)
        print(presicion)
        if presicion<0.85:
            print("Repita el comando")
    return comando
