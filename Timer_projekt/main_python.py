    # Timer
from time import *
import keyboard


print ('Prise Calculator')   
Start= input('Press (S) to Start and (X) to Stop: ')
keyboard.is_pressed("s")


h_now = strftime("%H")
m_now = strftime("%M")
s_now = strftime("%S")

time_f = 0
if int(s_now)-seconds>=0:
    time_f = int(s_now)-seconds
else:
    time_f = 60 - (seconds - int(s_now))
    m_now -=1

print(f"\nVon {h_now}:{m_now}:{time_f+1} bis {h_now}:{m_now}:{s_now}")