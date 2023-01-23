#Librerias
from API.api_key import *

def saludo(message):
    user_name= message.from_user.first_name
    chat_bot_key.send_message(chat_id=message.chat.id,text=f"Hola {user_name}")
