import cv2
import imutils
import time

faceCascade = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_alt2.xml')
# eyeCascade = cv2.CascadeClassifier('./haarcascade/haarcascade_eye.xml')


def detect(gray, frame):
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(100, 100),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]

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
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.putText(canvas, str, (0, 13), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))
    cv2.imshow('canvas', canvas)

    if cv2.waitKey(30) == 27:  # esc
        break

video_capture.release()
cv2.destroyAllWindows()
