import serial
arduino = serial.Serial('COM4', 9600)

while True:
    c = input()
    if c == 'q':
        break
    else:
        c = c.encode('utf-8')
        arduino.write(c)
