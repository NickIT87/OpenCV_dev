import cv2
import mediapipe as mp
import time


mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()
# default webcam detect
cap = cv2.VideoCapture(0)
pTime = 0
cTime = 0


def fpsframe():
    global pTime
    global cTime
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img,f'FPS: {int(fps)}',(10,40),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)


# infinity loop
while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    if results.detections:
        for id, detection in enumerate(results.detections):
            #mpDraw.draw_detection(img, detection)
            #print(id, detection)
            #print(detection.score)
            #print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img,bbox,(255,0,255),2)
            cv2.putText(img,
                        f'{int(detection.score[0]*100)}%',
                        (bbox[0],bbox[1]-20),cv2.FONT_HERSHEY_PLAIN,
                        2, (0,255,0), 2)

    fpsframe()
    cv2.imshow("Image", img)
    cv2.waitKey(1)