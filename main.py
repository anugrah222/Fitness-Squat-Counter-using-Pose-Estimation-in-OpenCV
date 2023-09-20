import cv2
import poseModule as pm
import numpy as np




cap = cv2.VideoCapture("/home/anugrah/vs_code/PROJECT/fitness_tracker/squat.mp4")

detector = pm.poseDetector()

count = 0 
dir = 0


while True:
    sucess,img = cap.read()
    img = cv2.resize(img,(1280,720))

    img = detector.findPose(img,draw=False)
    #print(img)

    lmlist = detector.findPosition(img,draw=False)
    #print(lmlist)

    if len(lmlist)!=0:
        angle1 = detector.findAngle(img,24,26,28,draw=False)
        #print(angle1)
        
        low = 40
        high = 170

        per = np.interp(angle1,(low,high),(0,100))
        #print(angle1, "----->" , per)

        if per == 0:
            
            if dir == 1:
                count+=0.5
                dir = 0

        if per == 100:
            
           if dir == 0:
               count+=0.5
               dir = 1


        #print(count)

        img = cv2.putText(img,str(int(count)),(50,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),3)
    cv2.imshow('fitness tracking',img)
    if cv2.waitKey(1) & 0XFF == 27:
        break