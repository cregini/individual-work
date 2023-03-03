from gpiozero import LED
from time import sleep

# This can be used to control your input and outoput fans as well

motor1 = LED(17) #Choose your pin here
motor2 = LED(27)
IRled1 = LED(24)

while True:
    IRled1.on()
    motor1.on() #turns LED on
    sleep(5)  #Choose duration here
    motor1.off() #turns LED off
    sleep(5) #choose frequency here
    
    motor2.on()
    sleep(5)
    motor2.off()
    IRled1.off()
    sleep(5)