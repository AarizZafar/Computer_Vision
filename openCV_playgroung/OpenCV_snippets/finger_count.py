import cv2
import HandTracking_max as htm
import mediapipe as mp
import os
import time

capture = cv2.VideoCapture(0)

capture.set(3,700)  # Setting the width of the window
capture.set(4,700)  # setting the hight of the window

path = "D:\\codes\\python\\opencv_proj\\finger_count_images"
myList = os.listdir(path)

# The image has to be over layed over the frame hence (OVER_LAY_IMAGE)

prevTime = 0
currTime = 0

detector = htm.handDetector(detectioncon=0.75)

overlayimage = []
for imPath in myList:
    image = cv2.imread(f"{path}/{imPath}") #
    # print(f"{path}\\{imPath}")
    overlayimage.append(image)


finger_tipID = [4,8,12,16,20]

# 4  - thum 
# 8  - index
# 12 - middle 
# 16 - ring 
# 20 - pinki 

while True:
    success, frame = capture.read()

    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame,draw=False)
    # print(lmList)

    if len(lmList) != 0:
        finger = []

        # THUMB
        if lmList[finger_tipID[0]][1] > lmList[finger_tipID[0]-1][1]:
            finger.append(1)
        else:
            finger.append(0)

        # 4 fingers 
        for id in range(1,5):
            if lmList[finger_tipID[id]][2] < lmList[finger_tipID[id]-2][2]:
                finger.append(1)
            else:
                finger.append(0)
        # printing which finger is up or dows [1 -> up , 0 -> down]
        # print(finger) 

        total_finger_count = finger.count(1)
        print("Number of fingers up : " , total_finger_count)

        hight , width , channel = overlayimage[total_finger_count-1].shape
        frame[0:hight,0:width] = overlayimage[total_finger_count-1]
        # list operation (-1) takes the last element of the list

        cv2.putText(frame, str(int(total_finger_count)),(45,324),cv2.FONT_HERSHEY_PLAIN,10,(71,53,12),25)

    currTime = time.time()
    fps = 1/(currTime - prevTime)
    prevTime = currTime

    cv2.putText(frame ,f"FPS : {int(fps)}",(200,400),cv2.FONT_HERSHEY_PLAIN,3,(71,168,175),2)

    cv2.imshow("Finger Count",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break