#Librerias
from API.api_key import *

def saludo(message):
    user_name= message.from_user.first_name
    chat_bot_key.send_message(chat_id=message.chat.id,text=f"Hola {user_name}! 😃")
    chat_bot_key.send_message(chat_id=message.chat.id,text=f"Me presento soy un chatbot, estoy a la orden para todas tus consultas")
    chat_bot_key.send_message(chat_id=message.chat.id,text=f"Si necesitas detalles de un producto que vistes en nuestras redes sociales solo envia una captura del producto que te gustó y listo")

