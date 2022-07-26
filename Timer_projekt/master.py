import startstop
import main
import threading
import stop
import time

def code1 ():
    import startstop

time.sleep(2)

def code2 ():
    import main 

time.sleep(2)

def code3 ():
    import stop



if __name__ == "__main__":
    stop()

threading.Thread(target=startstop.Start).start()

threading.Thread(target=main.time_start).start()    

threading.Thread(target=stop.Stop).start()  