from picamera2 import Picamera2
from libcamera import controls
from gpiozero import LED
import os
from time import sleep

picam2 = Picamera2() #creates a camera object
IRled1 = LED(24)
counter = 0 #variable to store picture count 

while True:
    picam2.start(show_preview=True) #Gives a preview window
    picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast}) #Allows camera to focus
    filename = ("Picture" + str(counter) + ".jpg") #declares a filename to differentiate pictures
    IRled1.on()
    picam2.start_and_capture_file(filename) #takes a picture and names it
    picam2.stop_preview() #turns off preview
    picam2.stop() #ends camera connection
    IRled1.off()
    os.system("v4l2-ctl --set-ctrl wide_dynamic_range=0 -d /dev/v4l-subdev0") #system call to end camera control
    
    counter+=1 #increments counter up by one
    sleep(10) #Choose your own frequency here
