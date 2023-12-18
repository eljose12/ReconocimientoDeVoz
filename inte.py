import pyttsx3
from reconocedor import *

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Configurar la velocidad del habla (rango entre 0 y 1)
engine.setProperty('rate', 120)

# Configurar el volumen (rango entre 0 y 1)
engine.setProperty('volume', 0.9)

class ConductorSintetizador:
    def __init__(self):
        self.en_servicio = False
        self.tarifas = {
            "cine": 12,
            "estacion": 14,
            "san simon": 17,
            "heladeria": 15,
            "plaza": 20,
            "mercado": 20
        }
        self.destino_actual = ""
        self.tarifa_actual = 0
    

    def procesar_comando(self, comando):
       

        if "hola" in comando:
            respuesta = "¡Hola! Soy tu conductor sintetizador. ¿En qué puedo ayudarte?"
        elif "servicio" in comando:
            self.en_servicio = True
            respuesta = "Sí, estoy en servicio. ¿A dónde te gustaría ir?"
        elif "bien" in comando:
            respuesta = "Sí joven, estoy bien."
        elif "cine" in comando:
            self.destino_actual = "cine"
            respuesta = "Sí, vamos al Cine Center."
        
        elif "cuanto" in comando:
            if self.destino_actual:
                self.tarifa_actual = self.tarifas.get(self.destino_actual, 0)
                respuesta = f"La tarifa sería de {self.tarifa_actual} bolivianos."
            else:
                respuesta = "Debes especificar un destino antes de preguntar por la tarifa."
        elif "estacion" in comando:
            self.destino_actual = "estacion"
            respuesta = "Sí, vamos a la Estación Policial."
        elif "san simon" in comando:
            self.destino_actual = "san simon"
            respuesta = "Sí, vamos a la Universidad San Simón."
        elif "heladeria" in comando:
            self.destino_actual = "heladeria"
            respuesta = "Sí, vamos a la Heladería Globos."
        elif "plaza" in comando:
            self.destino_actual = "plaza"
            respuesta = "Sí, vamos a la Plaza Principal."
        elif "mercado" in comando:
            self.destino_actual = "mercado"
            respuesta = "Sí, vamos al Mercado Hipermaxi."
        elif "rebaja" in comando:
            respuesta = "Ya joven, menos 2 bolivianos."
        elif "pare" in comando:
            respuesta = "Está bien joven, pararé en la esquina."
        elif "gracias" in comando:
            respuesta = "De nada joven."
        elif "adios" in comando:
            respuesta = "Adiós joven, un placer servirte."
        elif "no" in comando:
            self.destino_actual = ""
            self.tarifa_actual = 0
            respuesta = "Interacción actual anulada. ¿En qué más puedo ayudarte?"
        
        return respuesta

# Instanciar el conductor sintetizador
conductor = ConductorSintetizador()

# Bucle interactivo
while True:
    engine.say("Ingresa tu comando: ")
    engine.runAndWait()
    comando = escuchar_comando()
    respuesta = conductor.procesar_comando(comando)
    engine.say(respuesta)
    engine.runAndWait()
    print(respuesta)
    if comando == "adios":
        break
