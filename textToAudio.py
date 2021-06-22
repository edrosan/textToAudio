# Importamos el paquete
from gtts import gTTS 

mytext = "Hola Mundo"


language = "es"

tld = "com.mx"

tts = gTTS(text = mytext, lang = language, tld = tld, slow = False) 

tts.save("Example.mp3") 
