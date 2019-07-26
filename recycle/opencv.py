import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
index = 0
buf = [256]

while True:
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    buf = "C:\\Users\\reddit\\Project\\hanseithon-2\\recycle\\img\\img_%06d.jpg" % index
    cv2.imwrite(buf, frame)

    index = index + 1

    if index == 999999:
        index = 0

    if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()