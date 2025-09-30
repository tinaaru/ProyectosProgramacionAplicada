from machine import Pin
import time

# Lista de pines GPIO donde están conectados los LEDs
pines = [2, 5, 18, 19, 21, 22, 23, 25]

# Crear una lista de objetos Pin configurados como salida
leds = [Pin(pin, Pin.OUT) for pin in pines]

while True:
    # Recorrer cada LED de la lista
    for led in leds:
        led.value(1)       # Encender LED
        time.sleep(0.5)    # Esperar medio segundo
        led.value(0)       # Apagar LED
        time.sleep(0.1)    # Pequeña pausa antes del siguiente LED

