import cv2

capt = cv2.VideoCapture(0)
while True:
    _, frame = capt.read()
    cv2.imshow("image", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
