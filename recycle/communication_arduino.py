import serial, time
import cv2
from recycle.cloudvisreq import *

ser = serial.Serial(
    port='COM6',
    baudrate=9600,
)


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
index = 0
buf = [256]


while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    buf = "C:\\Users\\reddit\\Project\\hanseithon-2\\recycle\\img.jpg"
    cv2.imwrite(buf, frame)

    if index == 999999:
        index = 0

    result = run("AIzaSyCG6jmr1Ru6_PUE6s2esY-uGyI099TO728", ["img.jpg"])

    if "Developer" in result:
        ser.write("120".encode())
        time.sleep(1.5)
        ser.write("0".encode())

    print(result)


    if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()


while True:
    if ser.readable():
        res = ser.readline()
        print(res.decode()[:len(res)-1])

    ser.write("0".encode())
    print("insert degree :", end=' ')
    degree = input()
    ser.write(degree.encode())
    if int(degree) >= 70:
        time.sleep(1.5)