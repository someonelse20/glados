import RPi.GPIO as GPIO
import time
import potentiometer as pot

class stepper:
    def __init__(self, gpio, potentiometer):
        self.gpio = gpio
        self.pot_pin = potentiometer
        self.sequence = [
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1]
        ]

    def step(self, steps):
        pass

    def step_to_angle(self, angle):
        pass

