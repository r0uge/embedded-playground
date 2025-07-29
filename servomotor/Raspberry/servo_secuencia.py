# mover_servo_secuencia.py
# Permite el movimiento de un servo SG90 en el GPIO 23 en forma secuencial
# Utiliza implmentación de PWM basada en Hardware

from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import sys

# Define el pin GPIO al que está conectado el cable de señal del servo
# Por ejemplo, GPIO 18 (pin físico 12)
SERVO_PIN = 23

# Crea una instancia de la fábrica de pines pigpio para un control más suave
factory = PiGPIOFactory()

# Crea un objeto servo.
# Ajusta min_pulse_width y max_pulse_width si tu servo no alcanza el rango completo.
# Los valores típicos para SG90 son 0.0005 (0.5ms) y 0.0024 (2.4ms) para -90 a 90 grados.
servo = AngularServo(SERVO_PIN, min_angle=-90, max_angle=90, min_pulse_width=0.0005, max_pulse_width=0.0024, pin_factory=factory)

# Tiempo de pausa entre posiciones (segundos)
tiempo = 2

def secuencia_movimiento():
    """
    Realiza una secuencia de movimientos del servo:
    -90 -> 0 -> 90 con pausas de 2 segundos,
    y luego 90 -> 0 -> -90 con pausas de 2 segundos.
    """

    # Inicio de Secuencia = -90
    print("Moviendo a -90 grados...")
    servo.angle = -90
    sleep(tiempo)

    try:
        while True:
            print("Moviendo a 0 grados...")
            servo.angle = 0
            sleep(tiempo)

            print("Moviendo a 90 grados...")
            servo.angle = 90
            sleep(tiempo)

            # Secuencia 90 -> 0 -> -90
            print("Moviendo a 0 grados...")
            servo.angle = 0
            sleep(tiempo)

            print("Moviendo a -90 grados...")
            servo.angle = -90
            sleep(tiempo)

    except KeyboardInterrupt:
        print("\nSecuencia detenida por el usuario.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        # Es importante liberar los recursos GPIO al finalizar
        servo.close()
        print("Recursos GPIO liberados.")

if __name__ == "__main__":
    print("Iniciando secuencia de movimiento del servo. Presiona Ctrl+C para detener.")
    secuencia_movimiento()
