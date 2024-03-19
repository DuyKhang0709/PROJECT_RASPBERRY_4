import RPi.GPIO as GPIO
import time

LED_1_PIN = 17
LED_2_PIN = 27
LED_3_PIN = 22
BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_1_PIN, GPIO.OUT)
GPIO.setup(LED_2_PIN, GPIO.OUT)
GPIO.setup(LED_3_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

GPIO.output(LED_1_PIN, GPIO.LOW)
GPIO.output(LED_2_PIN, GPIO.LOW)
GPIO.output(LED_3_PIN, GPIO.LOW)

previous_button_state = GPIO.input(BUTTON_PIN)
lex_index = 0
while True:
    time.sleep(0.01)
    button_state = GPIO.input(BUTTON_PIN)
    if button_state != previous_button_state:
        previous_button_state = button_state
        if button_state == GPIO.HIGH:
            if lex_index == 0:
                lex_index = 1
                GPIO.output(LED_1_PIN, GPIO.HIGH)
                GPIO.output(LED_2_PIN, GPIO.LOW)
                GPIO.output(LED_3_PIN, GPIO.LOW)
            elif lex_index == 1:
                lex_index = 2
                GPIO.output(LED_1_PIN, GPIO.LOW)
                GPIO.output(LED_2_PIN, GPIO.HIGH)
                GPIO.output(LED_3_PIN, GPIO.LOW)
            else:
                lex_index = 0
                GPIO.output(LED_1_PIN, GPIO.LOW)
                GPIO.output(LED_2_PIN, GPIO.LOW)
                GPIO.output(LED_3_PIN, GPIO.HIGH)




GPIO.cleanup()