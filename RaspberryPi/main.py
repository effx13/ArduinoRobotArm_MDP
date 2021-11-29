import cv2
import imutils
import time
import time
import serial
import threading
import json
from serial.serialutil import SerialException

port = "COM3"
arduino = serial.Serial(port, 115200, timeout=1)
xyz = json.load('{"0":150,"1":45,"2":165}')
is_lock = False

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
                xyz = json.load(val)


def move_motor(x, y, z):
    is_lock = True
    send_serial([x, y, z])
    time.sleep(1)
    
    
# 초기화
send_serial([150, 45, 165])

thread = threading.Thread(target=readThread, args=(arduino,))
thread.start()
# 기본각도 150, 45, 165
# while True:
#     angs = [150, 45, 165]
#     send_serial(angs)


faceCascade = cv2.CascadeClassifier(
    'C:/Users/user/Git/ArduinoRobotArm_MDP/RaspberryPi/haarcascade/haarcascade_frontalface_alt2.xml')
# eyeCascade = cv2.CascadeClassifier('./haarcascade/haarcascade_eye.xml')


def detect(gray, frame):
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(100, 100),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]
        print(x, y)
        if x < 80:
            print("왼쪽으로 치우침")
        elif x > 150:
            print("오른쪽으로 치우침")

        if y < 40:
            print("위로 치우침")
        elif y > 80:
            print("아래로 치우침")
        # eyes = eyeCascade.detectMultiScale(face_gray, 1.1, 3)
        #
        #
        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    return frame


video_capture = cv2.VideoCapture(0)

prevTime = 0

while True:
    _, frame = video_capture.read()
    curTime = time.time()
    sec = curTime - prevTime
    prevTime = curTime
    fps = 1 / (sec)
    str = "FPS : %0.1f" % fps
    frame = imutils.resize(cv2.flip(frame, 1), width=320, height=240)
    # img = cv2.rectangle(frame, (40, 40), (140, 150), (0, 0, 255), 2)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.putText(canvas, str, (0, 13),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))
    cv2.imshow('canvas', canvas)
    if cv2.waitKey(30) == 27:  # esc
        break

video_capture.release()
cv2.destroyAllWindows()
