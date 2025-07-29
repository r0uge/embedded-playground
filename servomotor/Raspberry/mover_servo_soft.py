# mover_servo.py
# Permite el movimiento de un servo SG90 en el GPIO 23
# Utiliza implmentación de PWM basada en Sofware (genera un jitter/impresición al desplazarce)

from gpiozero import AngularServo
from time import sleep
import sys

# Define el pin GPIO al que está conectado el cable de señal del servo
# Puedes usar la numeración BCM o BOARD. Aquí usamos BCM (el número GPIO)
# Por ejemplo, GPIO 18 (pin físico 12)
SERVO_PIN = 23

# Crea un objeto servo.
# Ajusta min_pulse_width y max_pulse_width si tu servo no alcanza el rango completo.
# Los valores típicos para SG90 son 0.0005 (0.5ms) y 0.0024 (2.4ms) para 0-180 grados.
# Puedes necesitar ajustarlos para tu servo específico.
servo = AngularServo(SERVO_PIN, min_angle=-90, max_angle=90, min_pulse_width=0.0005, max_pulse_width=0.0024)

def mover_a_angulo(angulo):
    """
    Mueve el servo a un ángulo específico en grados (-90 a 90).
    -90 grados es un extremo, 0 es el centro, 90 es el otro extremo.
    """
    try:
        angulo = float(angulo)
        # Asegúrate de que el ángulo esté dentro del rango permitido por AngularServo (-90 a 90 por defecto)
        if -90 <= angulo <= 90:
            print(f"Moviendo servo a {angulo} grados...")
            servo.angle = angulo
            sleep(0.5) # Deja tiempo para que el servo se mueva
        else:
            print("Error: El ángulo debe estar entre -90 y 90 grados.")
            sys.exit(1)
    except ValueError:
        print("Error: El ángulo debe ser un número.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        angulo_deseado = sys.argv[1]
        mover_a_angulo(angulo_deseado)
    else:
        print("Uso: python3 mover_servo.py <angulo>")
        print("Ejemplo: python3 mover_servo.py 45")
        print("El ángulo debe estar entre -90 y 90 grados.")
        sys.exit(1)
