import requests
import os
import cv2

# Definir la URL de la API y tu API key
api_url = 'https://api.platerecognizer.com/v1/plate-reader/'
api_key = 'd39b74a5426d40930618746f302aa90c913c6547'  # Reemplaza con tu clave de API

# Función para tomar una foto con la cámara
def capture_photo():
    cap = cv2.VideoCapture(0)  # Abre la cámara (cambiar 0 a 1 si tienes múltiples cámaras)

    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return

    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar la imagen.")
        return

    cv2.imwrite("captured_photo.jpg", frame)
    cap.release()
    print("Foto capturada como captured_photo.jpg")

# Comprobar si la imagen existe en la ubicación especificada
image_path = "captured_photo.jpg"  # Ruta de la imagen capturada
if not os.path.exists(image_path):
    print(f'La imagen no se encuentra en la ruta especificada: {image_path}')
else:
    # Crear la solicitud POST
    headers = {
        'Authorization': f'Token {api_key}'
    }
    files = {'upload': ('image.jpg', open(image_path, 'rb'))}
    response = requests.post(api_url, headers=headers, files=files)

    # Obtener la respuesta JSON
    if response.status_code == 200:
        data = response.json()

        # Acceder al número de placa
        if "results" in data and data["results"]:
            plate_number = data["results"][0].get("plate", "No se encontró placa")
            print(f'Número de placa: {plate_number}')
        else:
            print('No se encontraron resultados de reconocimiento de placas en la imagen.')
    else:
        print(f'Error {response.status_code}: {response.text}')

# Captura una foto con la cámara y la envía a la API
while True:
    input("Presiona Enter para capturar una foto...")
    capture_photo()
