from gpiozero import Servo
import random as r
import threading
import time
import sys
import os

from drivers import potentiometer

servos = [Servo(0), Servo(0), Servo(0), Servo(0)] # Ignoring the baseplate, 0 is shoulder, 1 is elbow, 2 is neck up down, and 3 is neck side to side.
pots = [0, 0, 0, 0] # Potentiometers corosponding to the servos above, in the same order.

def get_pot_values():
    values = []
    for i in range(4):
        values.append(potentiometer.angle(pots[i]))
    return values

def record(emotion, delay=0, step_time=0.1, filename=None): # All times in secconds.
    for servo in servos:
        servo.value = None

    if filename == None:
        filename = str(len(os.listdir('movement/recordings/' + emotion)))

    print('Starting record of ' + emotion + '/' + filename + ' in ' + str(delay) + ' Seconds!')
    time.sleep(delay)
    print('Starting recording as soon as I move!')

    with open(filename, 'w') as file:
        pot_values = get_pot_values()
        for angle in pot_values:
            file.write(angle + ',')
        file.write('\n')

        while pot_values == get_pot_values():
            pass

        def record_tick(pot_values):
            for angle in pot_values:
                file.write(angle + ',')
            time.sleep(step_time)
            pot_values = get_pot_values()

        recording = threading.Thread(target=record_tick, args=pot_values)

        recording.start()

        input('Starting recording! Press enter to quit.')

        recording.join()

        print('Recording saved as ' + emotion + '/' + filename + '.')

def play_file(file, step_time=0.1):
    with open(file, 'r') as file:
        for line in file:
            positions = line.split(',')
            for i in range(4):
                servos[i].value = positions[i]
            time.sleep(step_time)

def play_emotion(emotion, step_time=0.1):
    try:
        play_file(r.choice(os.listdir('movement/recordings/' + emotion)), step_time)
        return True
    except:
        print("Warning: incorect emotion.")
        return False

