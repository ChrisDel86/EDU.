#to run the timer and clear the screen#
from decimal import Rounded
import os, time 


#to calculate prise
def prise_rechner():
    try:
        #variable 'distance' records inputed distance
        distance = float (input ('Please enter distance(km): '))
        #calculate the Fare 'distance in km'
        Fare = distance*0.25
        #sum of the fare and the base fee 
        finalfare = Fare+2 
        #display fare to the nearest 2 decimal place
        print ("-"*30,f"\nYour Fare is {round(finalfare,2)} €")
        #incase error, give message
    except:
        print ('*** Incorrect input ***')
        # wait 2 seconds for user to read error message 
        time.sleep(2)
        #clear the screen 
        os.system('clear')
        #call back fuction to enter details again 
    prise_rechner()
    #call function to start program
prise_rechner()