import time
import os

path = r'C:\Users\Фёдор\PycharmProjects\dump\\'
file_name = str("%s.txt" % (format(time.strftime("%Y.%m.%d - %H_%M_%S"))))
whole_path = os.path.join(path, file_name)
start_time = time.time()


def mult(x, y):
    int(x)*int(y)
    time.sleep(1)
    it_took = 'calculation lasted %s' % (time.time() - start_time)
    return it_took


def setup():
    with open(whole_path, 'w') as file:
        file.write(mult(44444444444, 55555555555))

setup()