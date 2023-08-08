import cv2
from cvzone.HandTrackingModule import HandDetector 

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon = 0.8,maxHands=2)

while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)  

        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  
            handType1 = hand1["type"]  

            if len(hands) == 2:
                hand2 = hands[1]
                lmList2 = hand2["lmList"] 
                handType2 = hand2["type"] 

                # lmlist[16]      ->   [12,34,-4]
                # lmlist[16][0:2] ->   [12,34]    -> we have to work on these values 

                length, info, img = detector.findDistance(lmList1[16][0:2], lmList2[16][0:2], img)  

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break