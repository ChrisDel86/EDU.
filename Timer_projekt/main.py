
import time
import sys
import keyboard
import threading




time_start =time.time()
hours = 0
seconds = 0
minutes = 0
 




print ('Prise Calculator')   
Start= input('Press (S) to Start and (X) to Stop: ')
keyboard.is_pressed("s")
if Start == 's':
    time_start = True
   


time_start =Start





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
    
        break

