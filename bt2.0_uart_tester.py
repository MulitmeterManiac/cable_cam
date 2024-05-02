from machine import UART, Pin
from time import sleep
from machine import Pin, PWM


uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
print('UART0:', uart)
print()

while True:
    if uart.any():
        data = uart.read().decode('utf-8')
        print(data)
