import sys
sys.path.append('/usr/local/lib/python3.11/site-packages/cv2/python-3.11')
import os
import cv2
from datetime import datetime

def tomar_foto(camara_index=0, ruta_guardado='/home/russell/Imágenes/takePhotoCustom'):
    # Verifica si la carpeta de imágenes existe, si no, la crea
    if not os.path.exists(ruta_guardado):
        os.makedirs(ruta_guardado)

    # Captura de video desde la cámara web
    captura = cv2.VideoCapture(camara_index)

    if not captura.isOpened():
        print("No se pudo abrir la cámara")
        return

    # Captura un solo fotograma
    ret, frame = captura.read()

    if not ret:
        print("No se pudo capturar la imagen")
        return

    # Obtiene la fecha y hora actual
    now = datetime.now()
    fecha_hora = now.strftime("%Y%m%d_%H%M%S")

    # Nombre del archivo concatenado con la fecha y hora
    nombre_archivo = f"foto_{fecha_hora}.jpg"

    # Ruta completa del archivo
    ruta_completa = os.path.join(ruta_guardado, nombre_archivo)

    # Guarda la imagen con el nombre concatenado en la carpeta especificada
    cv2.imwrite(ruta_completa, frame)

    # Libera la captura
    captura.release()
    print(f"Foto guardada en: {ruta_completa}")

if __name__ == "__main__":
    # Llama a la función para tomar la foto
    tomar_foto()
