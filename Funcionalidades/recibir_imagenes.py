
from API.api_key import *
import cv2
import os

def recibir_imagenes(message):
    file_id = message.photo[1].file_id
    file = chat_bot_key.get_file(file_id)
    decarga_archivo = chat_bot_key.download_file(file.file_path)
    primer_nombre_usuario = message.from_user.first_name
    datapath = "c:/Users/Administrador/Desktop/samsung/proyecto/Unnamed/BD"
    carpeta_guardada = datapath + "/" + primer_nombre_usuario
    if not os.path.exists(carpeta_guardada):
        os.mkdir(carpeta_guardada)
    else:
        print("La carpeta ya existe, no es necesario crearla")
    with open(carpeta_guardada + f"/imagen_Usuario.jpg","wb") as nuevo_archivo:
        nuevo_archivo.write(decarga_archivo)
    chat_bot_key.reply_to(message,"Estamos validando espere un momento ....")

    #Aqui leeremos la imagen enviada por el usuario
    lectura_de_imagen = cv2.imread(carpeta_guardada + f"/imagen_Usuario.jpg")
    while True:
        objeto = cv2.resize(lectura_de_imagen,(300,400))
        
