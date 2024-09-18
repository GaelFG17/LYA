import requests
from pprint import pprint

regions = ["mx", "us-ca"]  # Cambia a tu país
image_path = '/Users/gaelfranco/Downloads/prueba.jpeg'  # Ruta de tu imagen

with open(image_path, 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Opcional
        files=dict(upload=fp),
        headers={'Authorization': 'Token d39b74a5426d40930618746f302aa90c913c6547'})

    response_data = response.json()

    # Verifica si hay resultados y extrae la placa si existe
    if "results" in response_data and response_data["results"]:
        plate_number = response_data["results"][0].get("plate", "No se encontró placa")
        print(f'Número de placa: {plate_number}')
    else:
        print('No se encontraron resultados de reconocimiento de placas en la imagen.')

