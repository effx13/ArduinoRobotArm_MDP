import time
import serial
import threading
from serial.serialutil import SerialException

port = "COM3"
arduino = serial.Serial(port, 115200, timeout=1)


def send_serial(angle):
    c = str(angle[0]) + "," + str(angle[1]) + "," + str(angle[2])
    c = c.encode('utf-8')
    try:
        arduino.write(c)
        time.sleep(1)
    except SerialException:
        print("예외 발생")


def readThread(ser):
    while True:
        if ser.readable():
            val = ser.readline()
            val = val.decode()[:len(val)-1]
            if val != '':
                print(val)


thread = threading.Thread(target=readThread, args=(arduino,))
thread.start()

while True:
    angs = [90, 20, 90]
    for i in range(0, 181, 10):
        angs[0] = i
        send_serial(angs)
