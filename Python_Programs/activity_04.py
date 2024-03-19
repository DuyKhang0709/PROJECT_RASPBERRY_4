import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)

state = int(input("Enter 0 to power off the led , 1 to power on the led : "))
            
if state == 0:
            GPIO.output(LED_PIN, GPIO.LOW)
elif state == 1:
            GPIO.output(LED_PIN, GPIO.HIGH)
else:
            print("Wrong state value: " + str(state))
            GPIO.cleanup()
            exit
 
time.sleep(2)
GPIO.cleanup()