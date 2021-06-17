import cv2

# default webcam detect
cap = cv2.VideoCapture(0)

# infinity loop
while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)