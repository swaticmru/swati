import RPi.GPIO as GPIO
import time
def cam():
    b=1
    import os
    os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/Desktop/3.jpg")
    print("pic taken")  
GPIO.setmode(GPIO.BCM)
pirPin=6
GPIO.setup(pirPin, GPIO.IN)
counter=1
time.sleep(4)
while counter<=4:
     if GPIO.input(pirPin):
         print("motion detected")
         cam()
         time.sleep(1)
         counter = counter+1
print("testing")

