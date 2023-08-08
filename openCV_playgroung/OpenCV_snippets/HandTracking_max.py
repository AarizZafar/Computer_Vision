import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, model_comp=1,
                 detectioncon=0.5, trackconfi=0.5):

        self.mode = mode
        self.maxHands = maxHands
        self.detectioncon = detectioncon
        self.trackconfi = trackconfi
        self.model_comp = model_comp

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.model_comp,
                                        self.detectioncon, self.trackconfi)

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, frame, draw=True):
        RGB_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.result = self.hands.process(RGB_image)

        if (self.result.multi_hand_landmarks):
            for handsLMS in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handsLMS,
                                               self.mpHands.HAND_CONNECTIONS)

        return frame

    def findPosition(self, frame, handNo=0, draw=True):

        LandMarks_list = []
        if (self.result.multi_hand_landmarks):
            myHand = self.result.multi_hand_landmarks[handNo]

            for id, landMarks in enumerate(myHand.landmark):
                hight, width, channel = frame.shape
                x_pixel = int(landMarks.x*width)
                y_pixel = int(landMarks.y*hight)
                LandMarks_list.append([id, x_pixel, y_pixel])
                if draw:
                    cv2.circle(frame, (x_pixel, y_pixel), 7,
                               (100, 222, 68), cv2.FILLED)

        return LandMarks_list


def main():
    currTime = 0
    prevTime = 0

    capture = cv2.VideoCapture(0)

    detector = handDetector()

    while True:
        success, frame = capture.read()
        frame = detector.findHands(frame)
        LandMarks_list = detector.findPosition(frame)
        if len(LandMarks_list) != 0:
            print(LandMarks_list[4])

        currTime = time.time()
        fps = 1/(currTime - prevTime)
        prevTime = currTime

        cv2.putText(frame, str(int(fps)), (10, 70),
                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)

        cv2.imshow("Hand detection ", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
