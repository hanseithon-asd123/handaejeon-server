import serial, time, cv2, os
from recycle.cloudvisreq import *

ser = serial.Serial(
    port='COM6',
    baudrate=9600,
)

ser.write("0".encode())

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
index = 0


while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    buf = "C:\\Users\\reddit\\Project\\hanseithon-2\\recycle\\img.jpg"
    cv2.imwrite(buf, frame)

    result = run(os.environ.get('GOOGLE_API_KEY'), ["img.jpg"])

    product = ["자유시간", "청포도", "정포도", "마이쮸", "핫식스", "LOTTE", "HOT", "CROWN", "Mini"]

    for item in product:
        if item in result:
            #문열림
            ser.write("100".encode())
            time.sleep(2)
            ser.write("0".encode())
            break

    if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()