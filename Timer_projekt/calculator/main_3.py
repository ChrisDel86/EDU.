# Programm zur Berechnung des Preises eines Scooter fahr
import time
import sys
from datetime import datetime
import keyboard



# um das Zeitformat lesbar zu machen

def timeFormat(t_start,t_stop):
    format = "%H:%M:%S"
    t_start = t_start.strftime(format)
    t_stop = t_stop.strftime(format)

    return t_start, t_stop

# Formel zur Berechnung des Preises
def price(timeInp):
    unlock = 1.0
    preis = 0.20

    if timeInp>0:
        return unlock + (preis * (timeInp+1))   
    else:
        return unlock + preis


# Wenn 's' gedrückt wird, starte Wenn 'x' gedrückt wird, stoppe
def inputFunc():
    bool_start = None
    print('Price calculator')
    start = input('Press (S) to Start and (X) to Stop: ')
    keyboard.is_pressed('s')

    if start == 's':
        bool_start = True
    else:
        bool_start = False

    return bool_start


#timer 
def func_while(trueFals):
    hours = 0
    seconds = 0
    minutes = 0
    dt_1 = datetime.now()

    while trueFals:
        sys.stdout.write(
            "\r{hours} Hours {minutes} Minutes {seconds} Seconds".format(hours=hours, minutes=minutes, seconds=seconds))
        sys.stdout.flush()

        if (seconds <= 59):
            time.sleep(1)
            seconds += 1

            if (minutes <= 59 and seconds == 59 + 1):
                minutes += 1

                if (minutes == 60 and seconds == 59 + 1):
                    hours += 1
                    minutes = 0
                    seconds = 0

        else:
            seconds = 0

        if keyboard.is_pressed("x"):
            break

    dt_2 = datetime.now()
    dt_1, dt_2 = timeFormat(dt_1, dt_2)

    return dt_1, dt_2, minutes


# um zu bestimmen, welches Programm zuerst ausgeführt werden soll

if __name__ == "__main__":

    boolReturn = inputFunc()

    t_start, t_stop, minutes = func_while(boolReturn)


    print(f"\nStart: {t_start}")
    print(f"Stop: {t_stop}")
    print(f'Preis: {price(minutes)} €')
