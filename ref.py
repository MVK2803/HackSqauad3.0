import time
import threading 
import moviepy
from moviepy.editor import VideoFileClip
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

def con(filenam,k,lane_no,cc):
    clip=VideoFileClip(filenam)
    cap= clip.subclip(k,k+10)   #to divide the video into clips of 10 seconds
    frame_count=0    
    for frame in cap.iter_frames():
        if(frame_count%100==0):  #frame rate is 25 s
            bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov5')                  
            cc=cc+label.count('car')+label.count('truck')+label.count('motorcycle')+label.count('bus') 
            cccar=ccar+label.count('car')
            ccbus=ccbus+label.count('bus') 
            cctruck=cctruck+label.count('truck')
            ccbike=ccbike+label.count('motorcycle')
            print(cc)
        frame_count+=1 
    dicti[lane_no]=cc

    lc[lane_no-1]=cc

    
   
    
total_seconds=60
cc1=cc2=cc3=0   #lanewise car count
max1=0
lc=[0,0,0]    #lane count
p=[0,0,0]     #number of lane occurences
   
for k in range(0,total_seconds,10):
    dicti={1:cc1,2:cc2,3:cc3}
    t1 = threading.Thread(target=con, args=("road.mp4",k,1,cc1,))
    t2 = threading.Thread(target=con, args=("rush.mp4",k,2,cc2,)) 
    t3 = threading.Thread(target=con, args=("surveillance.m4v",k,3,cc3,)) 
    #t4 = threading.Thread(target=con, args=("4.mp4",k,4,cc4,))
    if (max1!=1):
        t1.start()
        t1.join()  
            
    if (max1!=2 ):
        t2.start() 
        t2.join()
            
    if (max1!=3 ):    
        t3.start() 
        t3.join()
            
    # if (max1!=4 ):    
    #     t4.start() 
    #     t4.join()
        
    max1=max(dicti,key=dicti.get)
    if(max1==1):
        lc[0]=0
        p[0]+=1
        cc2=lc[1]
        cc3=lc[2]
        #cc4=lc[3]
        dicti[1]=cc1
            
    if(max1==2):
        p[1]+=1
        cc1=lc[0]
        lc[1]=0
        cc3=lc[2]
        #cc4=lc[3]
        dicti[2]=cc2
            
    if(max1==3):
        p[2]+=1
        cc1=lc[0]
        cc2=lc[1]
        lc[2]=0
        #cc4=lc[3]
        dicti[3]=cc3
            
    # if(max1==4):
    #     p[3]+=1
    #     cc1=lc[0]
    #     cc2=lc[1]
    #     cc3=lc[2]
    #     lc[3]=0
    #     dicti[4]=cc4
    for i in p:
        if i>1:
            max1=p.index(min(p))+1
            p=[0,0,0]
    
    print("Green signal to lane number",max1)
    print(dicti)