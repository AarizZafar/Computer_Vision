import cv2
from cvzone.HandTrackingModule import HandDetector

# final code

capture = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8,maxHands=1)

constant_list = [0,0]

fan_flag = False
lights_flag = False

while True:
    success , image = capture.read()
    no_hands, frame = detector.findHands(image,flipType=True)
    
    if no_hands:
        if(no_hands[0]["type"] == "Left"):
            hand1 = no_hands[0]
            LeftCount_list = detector.fingersUp(hand1)
            total_finger_count = LeftCount_list.count(1)

            if(LeftCount_list == [0,1,0,0,0]):
                print("LIGHTS -> ON FLAG : ",lights_flag)
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"LIGHTS -> ON ",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                if(lights_flag == False):
                    constant_list[0] = 1
                    lights_flag = True

            elif(LeftCount_list == [0,1,1,0,0]):
                print("LIGHTS -> OFF FLAG : ",lights_flag)
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"LIGHTS -> OFF",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                if(lights_flag == True):
                    constant_list[0] = 0
                    lights_flag = False

            elif(LeftCount_list == [0,1,1,1,0]):
                print("FAN -> ON FLAG : ",fan_flag)
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"FAN -> ON ",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                if(fan_flag == False):
                    constant_list[1] = 1
                    fan_flag = True

            elif(LeftCount_list == [0,1,1,1,1]):
                print("FAN -> OFF FLAG ",fan_flag)
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"FAN -> OFF ",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                if(fan_flag == True):
                    constant_list[1] = 0
                    fan_flag = False

            elif(LeftCount_list == [1,1,1,1,1]):
                print("LIGHTS AND FANS -> ON")
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"LIGHTS AND FAN -> ON",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                fan_flag = True
                lights_flag = True
                constant_list[0] = 1
                constant_list[1] = 1

            elif(LeftCount_list == [0,0,0,0,0]):
                print("FANS AND LIGHTS -> OFF")
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"LIGHST AND FANS OFF",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                lights_flag = False
                fan_flag = False
                constant_list[0] = 0
                constant_list[1] = 0

        else:
            hand2 = no_hands[0]
            RightCount_list = detector.fingersUp(hand2)
            total_finger_count = RightCount_list.count(1)


            if(RightCount_list == [0,1,0,0,0]):
                print("LIGHTS -> ON")
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"LIGHTS -> ON ",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                if(lights_flag == False):
                    constant_list[0] = 1
                    lights_flag = True

            elif(RightCount_list == [0,1,1,0,0]):
                print("LIGHTS -> OFF")
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"LIGHTS -> OFF ",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                if(lights_flag == True):
                    constant_list[0] = 0
                    lights_flag = False

            elif(RightCount_list == [0,1,1,1,0]):
                print("FAN -> ON FLAG : ",fan_flag)
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"FAN -> ON ",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                if(fan_flag == False):
                    constant_list[1] = 1
                    fan_flag = True

            elif(RightCount_list == [0,1,1,1,1]):
                print("FAN -> OFF FLAG ",fan_flag)
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"FAN -> OFF ",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                if(fan_flag == True):
                    constant_list[1] = 0
                    fan_flag = False

            elif(RightCount_list == [1,1,1,1,1]):
                print("LIGHTS AND FANS -> ON")
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"LIGHTS AND FAN -> ON",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                fan_flag = True
                lights_flag = True
                constant_list[0] = 1
                constant_list[1] = 1

            elif(RightCount_list == [0,0,0,0,0]):
                print("FANS AND LIGHTS -> OFF")
                cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
                cv2.putText(frame,"LIGHST AND FANS OFF",(170,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
                fan_flag = False
                lights_flag = False
                constant_list[0] = 0
                constant_list[1] = 0
            
    else:
        print(constant_list)
        if(constant_list == [1,0]):
            cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
            cv2.putText(frame,"LIGHTS -> ON , FAN -> OFF",(150,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
        elif(constant_list == [0,1]):
            cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
            cv2.putText(frame,"LIGHTS -> OFF , FAN -> ON",(150,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
        elif(constant_list == [0,0]):
            cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
            cv2.putText(frame,"LIGHTS -> OFF , FAN -> OFF",(150,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)
        elif(constant_list == [1,1]):
            cv2.rectangle(frame,(120,420),(625,350),(197,167,102),-1)
            cv2.putText(frame,"LIGHTS -> ON , FAN -> ON",(150,400),cv2.FONT_HERSHEY_PLAIN,2,(127,255,0),2)

    cv2.imshow("Hand gesture control ",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
