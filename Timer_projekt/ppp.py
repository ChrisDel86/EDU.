from ast import While
from datetime import datetime
import time


# take input from the user
choice = input("press (S) to start:")
if choice in ('S'):
    Start = float(input("Enter letter"))
def getTime():
     now = datetime.now()
     return now
var1 = getTime()
time.sleep(5)
var2 = getTime() 
print("Zeit1:",var1)
print("Zeit2:",var2)
print('differenz:',var2-var1)

print ((var1-var2)*0,25 , "€")




  

  

