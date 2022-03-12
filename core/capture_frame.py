import cv2
from PIL import Image
from skimage.metrics import structural_similarity
import numpy as np

# loading videointo open-cv
capture=cv2.VideoCapture("test/video/demo0.mp4")


def purge_duplicate(img0, img1, threshold, i=0):
    sim, diff = structural_similarity(img0, img1, full=True)
    if(sim < threshold):
        return True
    else:
        return 

i=0
lag,frame=capture.read()
img0=frame
img0_bw=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
while(capture.isOpened()):
    
    img0=frame
    img0_bw=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    flag,frame=capture.read()
    if(flag==False):
        break
        
    img1=frame
    img1_bw=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    if (purge_duplicate(img0_bw, img1_bw, 0.65, i) == True):
        path='frame/'+str(i)+'.jpg'
        cv2.imwrite(path,img0)
        i+=1

capture.release()
# cv2.destroyAllWindows()
