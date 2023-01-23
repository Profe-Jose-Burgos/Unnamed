#librerias
import Funcionalidades.Saludo as saludo
from API.api_key import *

@chat_bot_key.message_handler(commands=['start'])
def saludo_chatbot(message):
    saludo.saludo(message)


chat_bot_key.polling()