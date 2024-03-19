import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import os

PIR_PIN = 4
LED_PIN = 17
LOG_FILE_NAME = "/home/duykhang0709/camera/photo_logs.txt"

def take_photo(camera):
    file_name = "/home/duykhang0709/camera/img_" + str(time.time()) + ".jpg"
    camera.capture(file_name)
    return file_name

def update_photo_log_file(photo_file_name):
    with open(LOG_FILE_NAME, "a") as f:
        f.write(photo_file_name)
        f.write("\n")

#Set up camera
camera = PiCamera()
camera.resolution = (720, 480)
camera.rotation = 180
print("Waiting 2 seconds to init the camera...")
time.sleep(2)
print("Camera setup OK.")

#Remove log file
if os.path.exists(LOG_FILE_NAME):
    os.remove(LOG_FILE_NAME)
    print("Log file removed.")
    
#GPIO set up
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)
print("GPIO set up OK.")

MOVEMENT_DETECT_TRESHOLD = 3.0
last_pir_state = GPIO.input(PIR_PIN)
movement_timer = time.time()
MIN_DURATION_BETWEEN_2_PHOTO = 60.0
last_time_taken_photo = 0

print("Everything has been set up.")

try:
    while True:
        time.sleep(0.01)
        pir_state = GPIO.input(PIR_PIN)
        if pir_state == GPIO.HIGH:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        if last_pir_state == GPIO.LOW and pir_state == GPIO.HIGH:
            movement_timer = time.time()
        if last_pir_state == GPIO.HIGH and pir_state == GPIO.HIGH:
            if time.time() - movement_timer > MOVEMENT_DETECT_TRESHOLD:
                if time.time() - last_time_taken_photo > MIN_DURATION_BETWEEN_2_PHOTO:
                    print("Take photo and send it by email")
                    photo_file_name = take_photo(camera)
                    update_photo_log_file(photo_file_name)
                    last_time_taken_photo = time.time()
        last_pir_state = pir_state
except KeyboardInterrupt:
    GPIO.cleanup()
        
