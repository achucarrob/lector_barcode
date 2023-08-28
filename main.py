from flask import Flask, Blueprint, render_template, request, url_for, redirect
import cv2 as cv
import numpy as np
from pyzbar import pyzbar
# from app import data 
# print(data)
# from routes.product import producto 

app = Flask(__name__)

# app.register_blueprint(producto)
# Crear una ruta con Blueprint
# producto = Blueprint("producto", __name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    # test = request.form['test']
    # En esta ruta quiero que si el method == post: cap_de_video se active
    if request.method == 'POST':
        cap_de_video = cv.VideoCapture(0)

        cap_de_video.set(cv.CAP_PROP_FRAME_WIDTH, 220)
        cap_de_video.set(cv.CAP_PROP_FRAME_HEIGHT, 140)

        while cap_de_video.isOpened():
            ret, frame = cap_de_video.read() # Reads webcam feeds

            if ret: # ret devuelve un valor booleano, True si un frame se leyo correctamente
                barcodes = pyzbar.decode(frame) # devuelve una grilla
                # print(frame)
                for barcode in barcodes:
                    ''' 
                    extract the bounding box location of the barcode and draw the
                    bounding box surrounding the barcode on the image
                    '''
                    (x, y, w, h) = barcode.rect
                    cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

                    # convertir a el codigo bytes a texto
                    barcodeData = barcode.data.decode("utf-8") 
                    barcodeType = barcode.type
                    # print(barcodeData)
                    # draw the barcode data and barcode type on the image
                    text = "{} ({})".format(barcodeData, barcodeType)
                    cv.putText(frame, text, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    # imprimir
                    # print("[INFO] found {} barcode: {}".format(barcodeType, barcodeData))

                    # url para consultar a la API  
                    global url
                    url = 'https://world.openfoodfacts.net/api/v2/product/{}'.format(barcodeData)
                    #  data = requests.get(url)
                    print(url)
                cv.imshow("Scanner", frame)

                if cv.waitKey(1) == ord("q"):
                    cap_de_video.release()
                    cv.destroyAllWindows()
                    break
            else: 
                break

    return render_template('index.html')

# Renderizar detalles del producto o "No se encuentra"
@app.route("/product", methods=['GET'])
def consultar_producto():
    data = requests.get(url).json()

    packagings = data['material']

    return render_template('packaging.html', packagings = packagings)