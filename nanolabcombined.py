from picamera2 import Picamera2
from libcamera import controls
import os
from time import sleep
import board
import adafruit_scd30
from gpiozero import LED
from gpiozero import AngularServo
import csv
import datetime

picam2 = Picamera2() #creates a camera object
counter = 0 #variable to store picture count
scd = adafruit_scd30.SCD30(board.I2C())#Creates a sensor object
motor1 = LED(17) #intake
motor2 = LED(16)#outake
IRled1 = LED(22) #declare IR lighting
IRled1 = LED(23) #declare IR lighting
IRled1 = LED(24) #declare IR lighting
IRled1 = LED(25) #declare IR lighting
servo = AngularServo(4, min_angle=-90, max_angle=90)

titles = ['Day', 'Hour', 'Temperature (C)', 'Humidity (%)', 'CO2 (PPM)']

with open ('data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(titles)

while True:
    picam2.start(show_preview=True) #Gives a preview window
    picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast}) #Allows camera to focus
    filename = ("Picture" + str(counter) + ".jpg") #declares a filename to differentiate pictures
    
    servo.angle=-70
    sleep(1)
    picam2.start_and_capture_file(filename) #takes a picture and names it
    picam2.stop_preview() #turns off preview
    picam2.stop() #ends camera connection
    os.system("v4l2-ctl --set-ctrl wide_dynamic_range=0 -d /dev/v4l-subdev0") #system call to end camera control
    counter+=1 #increments counter up by one
    sleep(2)
    servo.angle=0
    sleep(1)
    picam2.start_and_capture_file(filename) #takes a picture and names it
    picam2.stop_preview() #turns off preview
    picam2.stop()
    os.system("v4l2-ctl --set-ctrl wide_dynamic_range=0 -d /dev/v4l-subdev0") #system call to end camera control
    counter+=1
    sleep(2)
    servo.angle=70
    sleep(1)
    picam2.start_and_capture_file(filename) #takes a picture and names it
    picam2.stop_preview() #turns off preview
    picam2.stop()
    os.system("v4l2-ctl --set-ctrl wide_dynamic_range=0 -d /dev/v4l-subdev0")
    counter+=1 #increments counter up by one
    
    ct = datetime.datetime.now()
    day = ct.day
    hour = ct.hour
    co2= round(scd.CO2,1) #reads carbon dioxide
    temp = round(scd.temperature, 1) #reads temp in C
    humidity = round(scd.relative_humidity, 1) #reads relative humidity

    print("CO2: ", co2, "PPM")
    print("Temperature: ", temp, "degrees C")
    print("Humidity: ", humidity, "%")
    
    data = (day, hour, temp, humidity, co2)
    
    with open ('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    motor1.on()
    motor2.on()
    IRled1.on()

    sleep(5) #Choose your frequency here
    
    
    IRled1.off()
