# importar librerias
import cv2 as cv
import numpy as np

# objeto que captura el video, el valor cero es para usar la camara de la note, si hay otra camara el valor seria 1 o 2
cap_de_video = cv.VideoCapture(0)

# prueba de que se abre camara
if not cap_de_video.isOpened():
    print("No se abre la camara")
else:
    print("nice")

# Para obtener los valores de nuestra camara, esta parte no es necesaria en el codigo, es solamente para entender como funciona
ancho_builtin_cam = cap_de_video.get(cv.CAP_PROP_FRAME_WIDTH)
print(ancho_builtin_cam)
alto_builtin_cam = cap_de_video.get(cv.CAP_PROP_FRAME_HEIGHT)
print(alto_builtin_cam)

# Configuracion del frame que queremos que tenga nuestra camara, es mejor probar valores menores a los que tiene la cam built in, no se puede setear un valor menor a la mitad,
ancho_deseado = cap_de_video.set(cv.CAP_PROP_FRAME_WIDTH, 620) # devuelve un booleano
print(ancho_deseado)
alto_deseado = cap_de_video.set(cv.CAP_PROP_FRAME_HEIGHT, 440) # devuelve un booleano
print(alto_deseado)

# Abrir la camara
# Leer un codigo de barras

while cap_de_video.isOpened():
    ret, frame = cap_de_video.read() # Reads webcam feeds
    print(ret)
    cv.imshow("Scanner", frame)

    if cv.waitKey(1) == ord("q"):
        break

cap_de_video.release()
cv.destroyAllWindows()


