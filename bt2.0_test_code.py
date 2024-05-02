from machine import UART, Pin
from time import sleep
from machine import Pin, PWM


uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
print('UART0:', uart)
print()



i1 = Pin(14, Pin.OUT)
i2 = Pin(15, Pin.OUT)

#duty_cycle < 65.000
speed = PWM(Pin(4))
speed.freq(1000)

run = False


x = "1"
while True:
    if uart.any():
        data = uart.read().decode('utf-8')
        print(data)
        
        
        
        if data == "req_con_test":
            uart.write(x)
            x = int(x)
            x +=1
            x = str(x)
            
        if data == "on_all":
            run = True
        elif data == "off_all":
            run = False
        
        if data == 'on1':
            speed.duty_u16(65000)
            i1.on()
            i2.off()
            print("on")

        elif data =="off":
            i1.off()
            i2.off()
            print("off")

        if run == False:
            i1.off()
            i2.off()
        


#rxData = uart1.readline()
#print('Daten empfangen:', rxData.decode('utf-8'))
