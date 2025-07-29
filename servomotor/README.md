# Control de un Servo

Código necesario para controlar/mover un servo con diferentes placas de desarrollo. Cada carpeta representa un microcontrolador en que se encuentra el código, con su respectivo instructivo.

La intención es obtener un código base probado para poder aplicarlo en diferentes proyectos.

## Hardware
Utilizo un servo SG90 , pero el principio es el mismo para cualquier servo 
Características:

 - Tensión de operacion: 4.8v a 6v 
 - Torque: 1,8 kg*cm a 2,2 kg*cm 
 - Angulo (rango de rotación): 180° 
 - Corriente:
	 - Reposo = unos pocos mA
	 - Movimiento =  100mA - 250mA
	 - Stall (bloqueo) = 500mA - 700mA
 - Velocidad de Operacion: 0,09 seg/60° a 0,12 seg/60°

**Conexiones:** Tiene un conector de 3 pines con los siguientes colores de cableado estándar:

 -   **Marrón/Negro:** GND (Tierra)
 -   **Rojo:** VCC (Alimentación +5V)
 -   **Naranja/Amarillo/Blanco:** Señal (PWM)

**Modo de Control:** Se controla mediante una señal de **PWM (Pulse Width Modulation)**.
-   El servo espera un pulso cada 20 ms (50 Hz).
-   La duración del pulso determina la posición del eje:
    -   Aproximadamente **0.5 ms a 0.6 ms** para una posición extrema (ej. 0 grados o -90 grados).
    -   Aproximadamente **1.5 ms** para la posición central (90 grados o 0 grados).
    -   Aproximadamente **2.4 ms a 2.5 ms** para la otra posición extrema (180 grados o 90 grados).
