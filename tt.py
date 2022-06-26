import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import time
cap=cv2.VideoCapture('rush.mp4')
cc=0

while True:
    
    ret,frame1=cap.read()
    bbox, label, conf = cv.detect_common_objects(frame1, confidence=0.25, model='yolov3-tiny')
    cv2.imshow('Video Orginal',frame1)
    time.sleep(0.000005)
    if cv2.waitKey(1)==13:
        break
    cv2.waitKey(30)
    cc=cc+label.count('car')+label.count('truck')+label.count('motorcycle')+label.count('bus')
    print(cc)
cv2.destroyAllWindows()
cap.release()

    