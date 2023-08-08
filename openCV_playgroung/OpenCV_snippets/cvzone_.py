import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=2)

while True:
    success, image = cap.read()

    hands, img = detector.findHands(image, flipType=True)
    # hands = detector.findHands(image,draw=False) # No draw 

    # img - is with the drawing of the left and right hands detection 

    # hands - is the number of hands that has been detected 
    # hands = [ [hand1 = {}], [hand2 = {}], [hand3 = {}], ... .. .  ]
    #       - the hand1,2,3... will be an list that will have an dictionary inside it
    #       - The dict contains the information about the [lmList , bounding box, center, type(left ,right)]
    #         hand1,2,3... = dict{lmList - bounding box - center - type}

    if hands: 
        # getting the first hand 
        # we are basically getting all the information about the first hand all the land marks etc
        hand1            = hands[0]
        lmList1          = hand1["lmList"]           # list of 21 land marks
        bbox1            = hand1["bbox"]             # bounding box information x, y, w, h
        centerPoint1     = hand1["center"]           # center of the hand cx, cy
        handType1        = hand1["type"]             # the hand type if it is left or right
        finger1Count     = detector.fingersUp(hand1)  # counting the number of fingers that are up 

        # LEFT and RIGHT HAND FINGER LIST INDEX ->
        # [THUMB, INDEX FINGER, MIDDLE FINGER, RING FINGER, PINKI FINGER]

        

        print(handType1,finger1Count,"No fingers : ",len(finger1Count))

        # finding the distance between 2 land marks of the same hand
        # length, info , img = detector.findDistance(lmList1[2],lmList1[12],img)

        # if we are detecting 2 fingers
        if(len(hands) == 2):
            hand2          = hands[1]
            lmlist2        = hand2["lmList"]
            bbox           = hand2["bbox"]
            centerPoint2   = hand2["center"]
            handType2      = hand2["type"]
            finger2Count     = detector.fingersUp(hand2)
            print(handType1,finger1Count,"No fingers : ",len(finger1Count))
            print(handType2,finger2Count,"No fingers : ",len(finger2Count))

    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break