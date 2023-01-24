
from API.api_key import *
from Extras.Diccionario import *
import re #esta libreria es para las expresiones regulares
import unidecode
mensaje_recibido=""

def recibe_texto(message):
    global mensaje_recibido
    mensaje_recibido = message.text
    #convierto a minusculas
    convertidor_minuscula = mensaje_recibido.lower()
    #limpio el texto de los caracteres especiales
    #texto = re.sub(r'[^a-z0-9\s]','',convertidor_minuscula)
    texto = unidecode.unidecode(convertidor_minuscula)

    if texto in diccionario:
        busqueda= diccionario[texto]
        chat_bot_key.send_message(message.chat.id,busqueda)
    else:
        chat_bot_key.send_message(message.chat.id,"Un momento mi vocabulario no es muy amplio")


