
import time
import sys
from datetime import datetime
import keyboard




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