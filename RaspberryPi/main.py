import cv2
import imutils
import time
import threading
import serial
from serial.serialutil import SerialException

# -------------------변수 선언 부분-------------------
port = "/dev/ttyACM0"
readed = ""
reset_timer_seconds = -1
motor_timer_seconds = -1
angles = [150, 130, 170]
arduino = serial.Serial(port, 115200, timeout=1)
haarcascade_file = '/home/pi/ArduinoRobotArm_MDP/RaspberryPi/haarcascade/haarcascade_frontalface_alt2.xml'


# -------------------타이머 쓰레드 부분-------------------
def reset_timer():
    global reset_timer_seconds, angles
    while True:
        if reset_timer_seconds > 0:
            reset_timer_seconds -= 1
            time.sleep(1)
        if reset_timer_seconds == 0:
            angles = [150, 35, 165]
            print("자리 초기화")
            reset_timer_seconds = -1


# -------------------모터 제어 함수 부분-------------------
def send_serial(arduino):
    global angles
    while True:
        c = str(angles[0]) + "," + str(angles[1]) + "," + str(angles[2])
        c = c.encode('utf-8')
        try:
            arduino.write(c)
            time.sleep(0.25)  # 0.25초
        except SerialException:
            print("예외 발생")


def read_serial(arduino):
    global readed
    while True:
        if arduino.readable():
            val = arduino.readline()
            val = val.decode()[:len(val) - 1]
            if val != '':
                print(val)
                readed = val


# -------------------OpenCV 함수 부분-------------------
faceCascade = cv2.CascadeClassifier(haarcascade_file)

# eyeCascade = cv2.CascadeClassifier('./haarcascade/haarcascade_eye.xml')

def detect(gray, frame):
    global reset_timer_seconds
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.03, minNeighbors=5, minSize=(
        100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    face_count = len(faces)
    if face_count == 0:
        pass
    elif face_count == 1:
        for (x, y, w, h) in faces:
            reset_timer_seconds = 10
            center_x = int(x + w / 2)
            center_y = int(y + h / 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.line(frame, (center_x, center_y), (center_x, center_y), (0, 255, 0), 5)
            # face_gray = gray[y:y + h, x:x + w]
            # face_color = frame[y:y + h, x:x + w]
            if center_x < 110:
                print("왼쪽으로 치우침")
                if angles[0] > 10:
                    angles[0] -= 1
            elif center_x > 190:
                print("오른쪽으로 치우침")
                if angles[0] < 170:
                    angles[0] += 1
                angles[0] += 1
            if center_y < 80:
                print("위로 치우침")
                if angles[1] > 10:
                    angles[1] += 1
                    angles[2] += 1
            elif center_y > 160:
                print("아래로 치우침")
                if angles[1] < 170:
                    angles[1] -= 1
                    angles[2] -= 1
    else:
        print(f'{face_count}개의 얼굴이 감지됨')
    return frame


video_capture = cv2.VideoCapture(0)
prevTime = 0

# -------------------초기화 부분-------------------
read_thread = threading.Thread(target=read_serial, args=(arduino,))
read_thread.start()
send_thread = threading.Thread(target=send_serial, args=(arduino,))
send_thread.start()
timer_thread = threading.Thread(target=reset_timer)
timer_thread.start()

# -------------------반복문 부분-------------------
while True:
    _, frame = video_capture.read()
    curTime = time.time()
    sec = curTime - prevTime
    prevTime = curTime
    fps = 1 / sec
    fps = "FPS : %0.1f" % fps
    frame = imutils.resize(cv2.flip(frame, 1), width=320, height=240)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.rectangle(frame, (110, 160), (190, 80), (0, 0, 255), 2)
    cv2.putText(canvas, fps, (0, 13),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))
    cv2.imshow('canvas', canvas)
    if cv2.waitKey(30) == 27:  # esc
        break

video_capture.release()
cv2.destroyAllWindows()
