import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands               # Hands module
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, 1,
                                        self.detectionCon, self.trackCon)    # hand landmarks obj
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        # finger label colors
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c = img.shape  # c - channels of image
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    if id == 0:
                        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                    if id == 4 or id == 8 or id == 12 or id == 16 or id == 20:
                        cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList


def main():
    pTime = 0                   # fps var
    cTime = 0                   # fps var
    cap = cv2.VideoCapture(0)   # handle camera
    detector = HandDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])
        # ========= fps frame =============
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(
            img,  # camera image
            str(int(fps)),  # fps number
            (10, 70),  # position
            cv2.FONT_HERSHEY_PLAIN,  # font
            3,  # scale
            (255, 0, 255),  # color
            3  # thickness
        )  # ========= fps frame =============
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()