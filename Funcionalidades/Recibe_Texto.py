
from API.api_key import *
from Extras.Diccionario import *

mensaje_recibido=""

def recibe_texto(message):
    global mensaje_recibido
    mensaje_recibido = message.txt
    convertidor_minuscula = mensaje_recibido.lower()
    if convertidor_minuscula in diccionario:
        busqueda= diccionario[convertidor_minuscula]
        chat_bot_key.send_message(message.chat.id,busqueda)
    else:
        chat_bot_key.send_message(message.chat.id,"Un momento mi vocabulario no es muy amplio")
