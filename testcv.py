from PIL import Image
import cvlib as cv
from cvlib.object_detection import draw_bbox

clip=Image.open("test.jpg")
bbox, label, conf = cv.detect_common_objects(clip, confidence=0.25, model='yolov3-tiny')                  
cc=label.count('car')+label.count('truck')+label.count('motorcycle')+label.count('bus')
print(cc)