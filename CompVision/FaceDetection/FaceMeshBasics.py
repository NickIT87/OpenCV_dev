import cv2
import mediapipe as mp
import time


cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)


def fpsframe():
    global pTime
    global cTime
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'FPS: {int(fps)}',(10,40),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            # FACEMESH_TESSELATION <-> FACEMESH_CONTOURS
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION, drawSpec, drawSpec)
            
            for id, lm in enumerate(faceLms.landmark):
                #print(lm)
                ih, iw, ic = img.shape
                x,y = int(lm.x*iw), int(lm.y*ih)
                cv2.putText(img, str(id), (x,y), cv2.FONT_HERSHEY_PLAIN,
                                0.5, (0,255,0), 1)
                print(id, x, y)


    fpsframe()
    cv2.imshow("Image", img)
    cv2.waitKey(1)