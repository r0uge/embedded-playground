# DS14287  
Conexion del RTC Dallas DS14287 a un uC  


# Consideraciones  
Esta lectura accede a un registro del RTC (por ejemplo, los segundos).
No se incluye escritura, pero la lógica es similar (cambiar pines a salida y R/W a LOW).
El tiempo y las señales deben respetar los tiempos mínimos indicados en la hoja de datos del DS14287.  

# Conexiones  Arduino


|DS14287 Pin |	Arduino Pin |	Descripción|
| :-----------: | :-----------: | :-----------: |
|D0–D7 |	D2–D9	| Bus de datos bidireccional |
|A0, A1 |	D10, D11	| Dirección del registro |
|CS	| D12 |	Chip Select |
|AS	| D13	| Address Strobe |
|DS	| A0 |	Data Strobe |
|R/W | A1	| Read/Write (HIGH=read, LOW=write) |
|RESET | A2 | Reset|
|GND | GND	| Tierra|
|VCC | 5 V | Alimentación|

