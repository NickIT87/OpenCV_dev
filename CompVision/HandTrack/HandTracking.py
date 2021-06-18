import cv2
import time
import HandTrackingModule as htm


def main():
    pTime = 0                   # fps var
    cTime = 0                   # fps var
    cap = cv2.VideoCapture(0)   # handle camera
    detector = htm.HandDetector(maxHands=3)
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print("working", lmList[4])
        else:
            print("stopped")
        # ========= fps frame =============
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(
            img,                        # camera image
            str(int(fps)),              # fps number
            (10, 70),                   # position
            cv2.FONT_HERSHEY_PLAIN,     # font
            3,                          # scale
            (255, 0, 255),              # color
            3                           # thickness
        )  # ========= fps frame =============
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()