import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)           # handle camera
mpHands = mp.solutions.hands        # Hands module
hands = mpHands.Hands()             # hand landmarks obj
mpDraw = mp.solutions.drawing_utils
pTime = 0                           # fps var
cTime = 0                           # fps var


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # finger label colors
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape                 # c - channels of image
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)
                if id == 4 or id == 8 or id == 12 or id == 16 or id == 20:
                    cv2.circle(img, (cx, cy), 15, (255,0,0), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    # ========= fps frame =============
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(
        img,                    # camera image
        str(int(fps)),          # fps number
        (10,70),                # position
        cv2.FONT_HERSHEY_PLAIN, # font
        3,                      # scale
        (255,0,255),            # color
        3                       # thickness
    ) # ========= fps frame =============
    cv2.imshow("Image", img)
    cv2.waitKey(1)