import time
import serial
import threading
from serial.serialutil import SerialException

port = "COM4"
arduino = serial.Serial(port, 115200, timeout=1)


def send_serial(angle):
    c = str(angle[0]) + "," + str(angle[1]) + "," + str(angle[2])
    c = c.encode('utf-8')
    try:
        arduino.write(c)
        time.sleep(0.25)
    except SerialException:
        print("예외 발생")


def readThread(ser):
    while True:
        if ser.readable():
            val = ser.readline()
            val = val.decode()[:len(val) - 1]
            if val != '':
                print(val)


read_thread = threading.Thread(target=readThread, args=(arduino,))
read_thread.start()

angles = [150, 35, 165]
while True:
    angles[1] = int(input())
    angles[2] = int(input())
    send_serial(angles)
