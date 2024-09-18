import tkinter as tk
from PIL import ImageTk, Image
import Recog as Re
import conector as cn
import serial
import time

# Función para ejecutar el reconocimiento y autorización de placa
def procesar_placa():
    Re.capture_photo_from_phone_camera()
    Re.recognize_plate("captured_photo.jpg")
    conec = cn.conectar_db()
    cursor = conec.cursor()
    cursor.execute("SELECT * FROM placas WHERE num_placa = %s", (Re.placa,))
    resultado = cursor.fetchone()
    if resultado:
        resultado_label.config(text="Placa autorizada")
        arduino.write(b'1')
    else:
        resultado_label.config(text="Placa no autorizada")

# Función para capturar una foto
def capturar_foto():
    Re.capture_photo_from_phone_camera()
    image = Image.open("captured_photo.jpg")
    image = image.resize((300, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    foto_label.config(image=photo)
    foto_label.image = photo
    procesar_placa()

# Configuración de la interfaz
root = tk.Tk()
root.title("Sistema de Reconocimiento de Placas")

# Botón para capturar foto
capturar_btn = tk.Button(root, text="Capturar Foto", command=capturar_foto)
capturar_btn.pack(pady=10)

# Etiqueta para mostrar la foto capturada
foto_label = tk.Label(root)
foto_label.pack(pady=10)

# Etiqueta para mostrar el resultado del reconocimiento de placa
resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=10)

# Abre el puerto serial
arduino = serial.Serial('/dev/tty.usbmodem1301', 9600, timeout=1)
time.sleep(2)  # Espera a que se establezca la conexión

root.mainloop()
