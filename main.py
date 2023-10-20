from machine import Pin,PWM,UART #importing PIN and PWM
import time #importing time

#Defining UART channel and Baud Rate
uart= UART(0,9600)
       
# Defining motor pins
In1=Pin(6,Pin.OUT)
In2=Pin(7,Pin.OUT)

In3=Pin(4,Pin.OUT)
In4=Pin(3,Pin.OUT)
# Defining enable pins and PWM object
enable1=PWM(Pin(8))
enable2=PWM(Pin(2))

# Defining frequency for enable pins
enable1.freq(1000)
enable2.freq(1000)

# Setting maximum duty cycle for maximum speed (0 to 65025)
enable1.duty_u16(65025)
enable2.duty_u16(65025)

led = Pin(25, Pin.OUT)
led.toggle()
led1 = Pin(15, Pin.OUT)
led1.toggle()

# Forward
def turn_right():
    In1.low()
    In2.high()
    In3.high()
    In4.low()  
    
# Right
def turn_left():
    In1.high()
    In2.low()
    In3.low()
    In4.high()
    
# Backward
def move_forward():
    In1.low()
    In2.high()
    In3.low()
    In4.high()
    
# Forward
def move_backward():
    In1.high()
    In2.low()
    In3.high()
    In4.low()
    
#Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()

while True:
    if uart.any(): #Checking if data available
        data=uart.read() #Getting data
        data=str(data) #Converting bytes to str type
        print(data)
        if('forward' in data):
            move_forward() #Forward
        elif('backward' in data):
            move_backward() #Backward
        elif('right' in data):
            turn_right() #Turn Right
        elif('left' in data):
            turn_left() #Turn Left
        elif('stop' in data):
            stop() #Stop
        elif('E' in data):
            speed=data.split("|")
            print(speed[1])
            enable1.duty_u16(int(speed[1])) #Setting Duty Cycle
            enable2.duty_u16(int(speed[1])) #Setting Duty Cycle
        else:
            stop() #Stop
       


