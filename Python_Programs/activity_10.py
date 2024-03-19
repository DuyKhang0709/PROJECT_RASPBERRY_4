import os
import time
from picamera import PiCamera


FOLDER_NAME = "/home/duykhang0709/activity_10"

if not os.path.exists("/home/duykhang0709/activity_10"):
    os.mkdir("/home/duykhang0709/activity_10")
    
camera = PiCamera()
camera.resolution = (1280, 720)
camera.rotation = 180
time.sleep(2)

counter = 1

while True:
    file_name = FOLDER_NAME + "/img" + str(counter) + ".jpg"
    counter +=1
    camera.capture(file_name)
    print("Photo done")
    time.sleep(5)
    
