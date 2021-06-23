import time

def func():
    x = int(input('number of seconds '))
    while int(x) >= 0:
        time.sleep(x)
        x = int(input('number of seconds '))
    else:
        quit()

func()