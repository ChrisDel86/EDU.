


from faulthandler import disable
from random import choices

from keyboard import * 
import time
import sys
from turtle import back
import threading


time_start =time.time()
hours = 0
seconds = 0
minutes = 0



# Ask to Begin
# take input from the user
choice = input("press (S) to start and (X) to stop:")

def start():
    if choice in ('s'):
        time_start = float(input("Enter letter"))
    if choice == 's':
        time_start = True
    
    else:
        print("Invalid Input")




while time_start:
    
   
    sys.stdout.write("\r{hours} Hours {minutes} Minutes {seconds} Seconds".format(hours=hours, minutes=minutes, seconds=seconds))
    sys.stdout.flush()
   
    if (seconds <= 59):
        time.sleep(1)
        seconds += 1

        if (minutes <= 59 and seconds == 59 + 1):
            minutes += 1

            if (minutes == 60 and seconds == 59 + 1 ):
                hours += 1
                minutes = 0
                seconds = 0
      
    
    else:
       seconds = 0


    if choice in ('x'):
        time_start = float(input("Enter letter"))
    if choice == 'x':
        time_start = False
        break
    
    

sys.stdout.write("\r{hours} Hours {minutes} Minutes {seconds} Seconds".format(hours=hours, minutes=minutes, seconds=seconds))

time_start= False



      
    

threading.Thread(target=time_start).start()
threading.Thread(target=choice).start()