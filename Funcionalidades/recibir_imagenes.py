
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
    
    imagen_base = cv2.resize(lectura_de_imagen,(300,400))
    
    imagen_de_referencia = cv2.imread("c:/Users/Administrador/Desktop/samsung/proyecto/Unnamed/air_jordan.jpg")
    imagen = cv2.resize(imagen_de_referencia,(300,400))
    
    resultado = cv2.matchTemplate(imagen,imagen_base, cv2.TM_CCOEFF_NORMED)
    minimo_valor,maximo_valor,minimo_loc,maximo_loc = cv2.minMaxLoc(resultado)
    
    if maximo_valor > 0.7:
        print("Imagen encontrada en la BD")
        chat_bot_key.send_message(chat_id=message.chat.id, text=f"""Descripción\nZapatos de Hombres\nCierre mediantes cordones a contraste\n100% de algodon.
        \nDETALLES\nMarca:NIKE\nModelo:Nike Air Jordan 1 Chicago\nPrecio:110.00$ + ITBMS\nTalla:40,39,38,37\nTenemos 100 Unidades\nSolo en las sucursales de Chiriqui,Marvella.
        \nCUIDADOS\nLimpiar con paño humedo\nLimpiar con cepillo suave""")
        chat_bot_key.send_message(chat_id=message.chat.id,text=f"si desea comprar el producto escribe /si")

    else:
        print("La imagen no se encuentra en nuestra BD")
        chat_bot_key.send_message(chat_id=message.chat.id,text=f"El producto enviado no coincide con ninguno del stock ❌, vuelve a intentarlo por favor")
    return recibir_imagenes

