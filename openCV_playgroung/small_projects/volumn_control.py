import cv2
import time
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import math
import pycaw
# --------------------------------------------------------------------------
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)  # setting the volume of the computer
minVol = volRange[0]
maxVol = volRange[1]
# ----------------------------------------------------------------------------

detector = HandDetector(detectionCon=0.8,maxHands=1)

cap = cv2.VideoCapture(0)

#                    numeric representation
# cv2.CAP_PROP_FRAME_WIDTH   (3)
# cv2.CAP_PROP_FRAME_HEIGHT  (4)

cap.set(3, 700)
cap.set(4, 700)

prev_time = 0

while True:
    success, img = cap.read()

    hands, img = detector.findHands(img,flipType=True)

    if hands:
        hands1            = hands[0]
        lmList1           = hands1["lmList"]

        thumb_x,thumb_y = lmList1[4][0],lmList1[4][1]
        index_x,index_y = lmList1[8][0],lmList1[8][1]

        center_x,center_y = (index_x + thumb_x)//2,(index_y+thumb_y)//2


        cv2.circle(img,(thumb_x,thumb_y),10,(127, 255, 0),cv2.FILLED)
        cv2.circle(img,(index_x,index_y),10,(127, 255, 0),cv2.FILLED)

#       DRAWING LINE BETWEEN THUMB AND INDEX FINGER
        cv2.line(img,(index_x,index_y),(thumb_x,thumb_y),(255,144,30),3)

# ----------------------------------------------------------------------------------
#     ^  (x1,y1)
#     |     |\        
#     |     | \
#     |     |  \
#     |     |   \
#  (y2-y1)  |    \
#     |     |     \
#     |     |      \
#     |     |_______\
# ALTITUDE          (x2,y2)
#               
#           <-(x2-x1)->  BASE
# -----------------------------------------------------------------------------------

#       CENTER POINT BETWEEN THE LINE DRAWN 
        cv2.circle(img,(center_x,center_y),10,(211,0,148),cv2.FILLED)

        length = math.hypot(thumb_x-index_x,thumb_y-index_y)
        
        if length < 50:
            cv2.circle(img,(center_x,center_y),10,(128,0,0),cv2.FILLED)

        # hand range   ->   50 - 300
        # volume range ->  -65 - 0 


        # converting the hand raneg to volume range
        vol = np.interp(length,[50,170],[minVol,maxVol])
        print(vol)

        volume.SetMasterVolumeLevel(vol,None)

    curr_time = time.time()
    fps = 1/(curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(img, f"FPS : {int(fps)}", (40, 70),cv2.FONT_HERSHEY_PLAIN, 2, (127, 255, 0), 2)

    cv2.imshow("image", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
