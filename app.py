# # importar librerias
# import cv2 as cv
# # print(cv.__version__)
# import numpy as np
# from pyzbar import pyzbar


# # objeto que captura el video, el valor cero es para usar la camara de la note, si hay otra camara el valor seria 1 o 2
# cap_de_video = cv.VideoCapture(0)

# # prueba de que se abre camara
# if not cap_de_video.isOpened():
#     print("No se abre la camara")
# else:
#     print("nice")

# # Para obtener los valores de nuestra camara, esta parte no es necesaria en el codigo, es solamente para entender como funciona
# ancho_builtin_cam = cap_de_video.get(cv.CAP_PROP_FRAME_WIDTH)
# print(ancho_builtin_cam)
# alto_builtin_cam = cap_de_video.get(cv.CAP_PROP_FRAME_HEIGHT)
# print(alto_builtin_cam)

# # Configuracion del frame que queremos que tenga nuestra camara, es mejor probar valores menores a los que tiene la cam built in, no se puede setear un valor menor a la mitad,
# ancho_deseado = cap_de_video.set(cv.CAP_PROP_FRAME_WIDTH, 220) # devuelve un booleano
# # print(ancho_deseado)
# alto_deseado = cap_de_video.set(cv.CAP_PROP_FRAME_HEIGHT, 140) # devuelve un booleano
# # print(alto_deseado)

# # Abrir la camara
# # Leer un codigo de barras

# while cap_de_video.isOpened():
#     ret, frame = cap_de_video.read() # Reads webcam feeds

#     if ret: # ret devuelve un valor booleano, True si un frame se leyo correctamente
#         barcodes = pyzbar.decode(frame) # devuelve una grilla
#         # print(frame)
#         for barcode in barcodes:
#             ''' 
#             extract the bounding box location of the barcode and draw the
# 	        bounding box surrounding the barcode on the image
#             '''
#             (x, y, w, h) = barcode.rect
#             cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

#             # convertir a el codigo bytes a texto
#             barcodeData = barcode.data.decode("utf-8") 
#             barcodeType = barcode.type
#             # print(barcodeData)
#             # draw the barcode data and barcode type on the image
#             text = "{} ({})".format(barcodeData, barcodeType)
#             cv.putText(frame, text, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#             # imprimir
#             print("[INFO] found {} barcode: {}".format(barcodeType, barcodeData))

#             # url para consultar a la API  
#             url = 'https://world.openfoodfacts.net/api/v2/product/{}'.format(barcodeData)
#             # data = requests.get(url)
#             print(url)
#         cv.imshow("Scanner", frame)
        
#         if cv.waitKey(1) == ord("q"):
#             break
#     else: 
#         break



# cap_de_video.release()
# cv.destroyAllWindows()





