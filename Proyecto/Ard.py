import Recog as Re
import conector as cn
import serial
import time

# Abre el puerto serial (ajusta el nombre del puerto según tu configuración)
arduino = serial.Serial('/dev/tty.usbmodem1301', 9600, timeout=1)
time.sleep(2)  # Espera a que se establezca la conexión

# Envía comandos al Arduino para mover el servo
while True:
    input("Presiona Enter para capturar una foto desde la cámara del teléfono...")
    Re.capture_photo_from_phone_camera()
    Re.recognize_plate("captured_photo.jpg")
    conec = cn.conectar_db()
    cursor = conec.cursor()

    cursor.execute("SELECT * FROM placas WHERE num_placa = %s", (Re.placa,))
    resultado = cursor.fetchone() 

    if resultado:
        print("Placa autorizada")
        arduino.write(b'1')
    else:
        print("Placa no autorizada")
