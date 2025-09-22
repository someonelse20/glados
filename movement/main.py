from gpiozero import Servo
import random as r
import time
import os

from drivers import potentiometer
import tracking

servos = [Servo(0), Servo(0), Servo(0), Servo(0)] # Ignoring the baseplate, 0 is shoulder, 1 is elbow, 2 is neck up down, and 3 is neck side to side.
pots = [0, 0, 0, 0] # Potentiometers corosponding to the servos above, in the same order.

def get_pot_values():
    values = []
    for i in range(4):
        values.append(potentiometer.angle(pots[i]))
    return values

def record(emotion, delay=0, step_time=0.01, filename=None): # All times in secconds.
    for servo in servos:
        servo.value = None

    print('Starting recording in ' + str(delay) + ' Seconds!')
    time.sleep(delay)
    print('Starting recording as soon as I move!')

    if filename == None:
        filename = len(os.listdir('movement/recordings/' + emotion))

    with open(filename, 'w') as file:
        starting_pot_values = get_pot_values()
        for angle in starting_pot_values:
            file.write(angle + ',')

        while starting_pot_values != get_pot_values():
            pass



def play_file(file):
    pass

def play_emotion(emotion):
    try:
        play_file(r.choice(os.listdir('movement/recordings/' + emotion)))
        return True
    except:
        print("Warning: incorect emotion.")
        return False

