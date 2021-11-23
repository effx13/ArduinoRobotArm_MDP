import time
import serial
from serial.serialutil import SerialException


port = "\\\\.\\COM4"
arduino = serial.Serial(port, 9600)

while True:
    c = input()
    if c == 'q':
        break
    else:
        c = c.encode('utf-8')
        try:
            arduino.write(c)
        except SerialException:
            print("예외 발생")
            time.sleep(100)


    if arduino.readable():
        val = arduino.readline()
        print(val.decode()[:len(val)-1])
