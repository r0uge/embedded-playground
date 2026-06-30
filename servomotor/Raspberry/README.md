# Control de un Servo con Raspberry

Código necesario para controlar/mover un servo con diferentes placas de desarrollo. Cada carpeta representa un microcontrolador en que se encuentra el código, con su respectivo instructivo.

La intención es obtener un código base probado para poder aplicarlo en diferentes proyectos.

## Conexionado
Como el SG90 tiene muy bajo consumo, aprovecho la misma alimentación de la Raspberry Pi, utilizando +5V y GND que cubre su capacidad de corriente sin problema. 
En caso de utilizar otro tipo de servo, es importante validar la corriente que requiere ya que puede ser necesario utilizar un fuente externa. 

> **Importante:** la masa la raspberry debe ser la misma que la fuente
> externa, para estar al mismo nivel de referencia (0v)

Para la conexión de la Señal utilizo el pin **GPIO 23**

## Librería
Se emplea la librería `gpiozero` por su facilidad  y abstracción

Para su instalación:

    sudo apt install python3-gpiozero python3-pigpio 
    sudo systemctl enable pigpiod 
    sudo systemctl start pigpiod



## Parámetros

Para ejecutar el código, requiere el parámetro del ángulo (desde -90° a 90°)

    python3 mover_servo.py 0     # Mueve al centro (0 grados)
    python3 mover_servo.py 45    # Mueve a 45 grados
    python3 mover_servo.py -90   # Mueve a un extremo (-90 grados)
    python3 mover_servo.py 90    # Mueve al otro extremo (90 grados)

> El angulo se limitó ya que el SG90 solo gira desde 0° a 180°

## Variables Importantes
Variables dentro del código que permite el ajuste para otros servos y/o conexiones

 - `SERVO_PIN =` Indica el PIN de la Raspberry donde se conecta la señal a
   enviar al Servo 
 - `servo =` dentro de la función `AngulaServo`
	 -  `min_angle`  y `max_angle`indica el ángulo mínimo de giro (inicio del rango) y ángulo máximo de giro (final del rango)
	 -  `min_pulse_width` y `max_pulse_width` Representan la duración mínima y máxima del pulso en  segundos.
