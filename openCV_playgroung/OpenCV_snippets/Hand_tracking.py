import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0)

mpHands = mp.solutions.hands

mpDraw = mp.solutions.drawing_utils
# By default solution to connect the land marks in a particular order 

hands = mpHands.Hands(max_num_hands=5,min_detection_confidence=0.5,min_tracking_confidence=0.5)
# static_image_mode       =  False (by default) prevent repeated detection
# max_num_hands           =  2 (by default)
# min_detection_confidenc =  0.5 (threshold for first frame)
# min_tracking_confidence =  0.5 (threshold for tracking frame)

currTime = 0
prevTime = 0

while  True:
    success, frame = capture.read()
    # web_cam = BGR
    # mediapip = RGB
    RGB_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    # rendering the image
    result = hands.process(RGB_image)

    # print(result.multi_hand_landmarks)
    if (result.multi_hand_landmarks):
        for handsLMS in result.multi_hand_landmarks:
            print("id  x  y")
            # printing the x ,y pixel value for all the 21 landmarks
            for id, landMarks in enumerate(handsLMS.landmark):
                hight, width, channel = frame.shape
                x_pixel = int(landMarks.x*width)                                  # X pixel value   
                y_pixel = int(landMarks.y*hight)                                  # y pixel value 
                print(id,x_pixel,y_pixel)
                if id==6:
                    cv2.circle(frame,(x_pixel,y_pixel),10,(148,114,68),cv2.FILLED)

            mpDraw.draw_landmarks(frame,handsLMS,mpHands.HAND_CONNECTIONS)
    
    currTime = time.time()
    fps = 1/(currTime - prevTime)
    prevTime = currTime

    cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)

    cv2.imshow("Hand detection ",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



