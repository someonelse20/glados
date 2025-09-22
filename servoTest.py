from gpiozero import Servo
import RPi.GPIO as gp

servo = Servo(10)

servo.value = 0
