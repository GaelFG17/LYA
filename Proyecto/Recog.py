import cv2
import requests
from pprint import pprint

# Configuración
api_token = 'Token d39b74a5426d40930618746f302aa90c913c6547'  
phone_camera_url = "http://192.168.1.24:8080/video"  
regions = ["mx", "us-ca"]  
# Función para capturar una foto desde la transmisión de la cámara
def capture_photo_from_phone_camera():
    cap = cv2.VideoCapture(phone_camera_url)

    if not cap.isOpened():
        print("No se pudo acceder a la transmisión de la cámara del teléfono.")
        return

    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar la imagen desde la cámara del teléfono.")
        return

    cv2.imwrite("captured_photo.jpg", frame)
    cap.release()
    print("Foto capturada desde la cámara del teléfono como captured_photo.jpg")

# Función para enviar la imagen a la API de Plate Recognizer
def recognize_plate(image_path):
    global placa
    placa = ""
    with open(image_path, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            data=dict(regions=regions),
            files=dict(upload=fp),
            headers={'Authorization': 'Token d39b74a5426d40930618746f302aa90c913c6547'}
        )


    response_data = response.json()

    # Verifica si hay resultados y extrae la placa si existe
    if "results" in response_data and response_data["results"]:
        plate_number = response_data["results"][0].get("plate", "No se encontró placa")
        placa = plate_number
        print(f'Número de placa: {plate_number}')
    else:
        print('No se encontraron resultados de reconocimiento de placas en la imagen.')

# Captura una foto desde la cámara del teléfono y la envía a la API
