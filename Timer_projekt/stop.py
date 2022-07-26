
import main
import startstop
import keyboard
import sys


choice = input ('x')


    
def Stop():

    while True:
    #take input from user 
        if choice == 'x':
            if keyboard.is_pressed("x", main.time_start):
                sys.exit
            break
        else:
           print("Invalid Input")