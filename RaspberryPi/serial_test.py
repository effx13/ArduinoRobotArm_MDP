import time
import serial
import threading
import json
from serial.serialutil import SerialException

port = "COM3"
arduino = serial.Serial(port, 115200, timeout=1)

def send_serial(angle):
    angles = {}
    angles["0"] = angle[0]
    angles["1"] = angle[1]
    angles["2"] = angle[2]
    c = json.dumps(angles)
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
    for i in range(0, 181, 30):
        send_serial([i, i, i])
    
