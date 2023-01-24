#librerias
import Funcionalidades.Saludo as saludo
import Funcionalidades.Recibe_Texto as rec_text
import Funcionalidades.recibir_imagenes as rec_images
import Funcionalidades.cotizacion as cot
from API.api_key import *


@chat_bot_key.message_handler(commands=['start'])
def saludo_chatbot(message):
    saludo.saludo(message)

@chat_bot_key.message_handler(content_types=["text"])
def recibe_texto_chatbot(message):
    rec_text.recibe_texto(message)

@chat_bot_key.message_handler(content_types=['photo'])
def recibir_foto_chatbot(message):
    rec_images.recibir_imagenes(message)

@chat_bot_key.message_handler(commands=['si'])
def cot_chatbot(message):
    chat_bot_key.send_message(chat_id=message.chat.id,text=f"Esta bien, te enviaremos la cotizacion en un momento.")
    cot.generate_invoice(message)
chat_bot_key.polling()