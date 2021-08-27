
import cv2
import mediapipe as mp
import time


class hand_detector_func():
    def __init__(self,mode=False,maxHands=10,detectConf=0.5,trackConf=0.5):

        self.mode = mode
        self.maxHands = maxHands
        self.detectConf = detectConf
        self.trackConf = trackConf

        self.mp_hand = mp.solutions.hands
        self.hands = self.mp_hand.Hands(self.mode,self.maxHands,self.detectConf,self.trackConf)
        self.mp_draw = mp.solutions.drawing_utils

        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self,image,draw=True):
        image_color= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.detection = self.hands.process(image_color)
    
        #print location of detections
        #uncomment to see
        #print(detection.multi_hand_landmarks)

        #loop through all hand images
        if self.detection.multi_hand_landmarks :
            for hand_landmrk in self.detection.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(image,hand_landmrk,self.mp_hand.HAND_CONNECTIONS)
        return image


    def findPosition(self,image,handNos=0,draw = True):

        self.landmark_list = []
        #loop through all hand images
        if self.detection.multi_hand_landmarks :
            myHand = self.detection.multi_hand_landmarks[handNos]
            for id,landMrk in enumerate(myHand.landmark):
            #print(f'details of each hand:\n'\f'id : {id}\n{landMrk}')
                #dimensions of image feed with height and width
                height_img,width_img,channel_img = image.shape

                #finding position of center on image
                center_x,center_y = int(landMrk.x*width_img), int(landMrk.y*height_img)

                self.landmark_list.append([id,center_x,center_y])

                if draw and id == 4:
                    cv2.circle(image,(center_x,center_y),10,(255,0,0),cv2.FILLED)
       
        return self.landmark_list
            #print(f'Dimensions of image in terms of pixels:\n'\f'id:{id}\n'\f'{center_x}\n{center_y}')

    
    def fingerUp(self):
        fingers = []
        #! Thumb
        if self.landmark_list[self.tipIds[0]][1] < self.landmark_list[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        #! Remaining 4 Fingures
        for id in range(1, 5):
            if self.landmark_list[self.tipIds[id]][2] < self.landmark_list[self.tipIds[id] - 2][2]:
                # 1-> when open
                fingers.append(1)
            else:
                # 0 ->when closed
                fingers.append(0)

        return fingers







def main():
    #frame rates
    prev_time = 0
    curr_time = 0
    
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    #call hand_detector_func
    detector = hand_detector_func()

    while True:
        result, image = capture.read()

        image = detector.findHands(image)

        landmark_list = detector.findPosition(image)

        print("location of thumb point:")
        if len(landmark_list) != 0:
            print(landmark_list[4])

        curr_time = time.time()
        fps = 1/(curr_time-prev_time)
        prev_time = curr_time

        cv2.putText(image,str(round(fps)),(0,35),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

        cv2.imshow("Hand tracking",image)
        #to quit press "q" wait for 10 sec
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # closes the window
    capture.release()

    # destroy or close the gui window
    cv2.destroyAllWindows()
    print("window closed")

if __name__ == "__main__":
    main()