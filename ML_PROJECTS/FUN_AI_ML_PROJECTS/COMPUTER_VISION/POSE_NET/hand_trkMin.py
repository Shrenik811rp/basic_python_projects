
import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)


mp_hand = mp.solutions.hands
hands = mp_hand.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.8)

mp_draw = mp.solutions.drawing_utils

#frame rates
prev_time = 0
curr_time = 0

while True:
    result, image = capture.read()

    image_color= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    detection = hands.process(image_color)

    #print location of detections
    #uncomment to see
    #print(detection.multi_hand_landmarks)


    #loop through all hand images
    if detection.multi_hand_landmarks :
        for hand_landmrk in detection.multi_hand_landmarks:
            mp_draw.draw_landmarks(image,hand_landmrk,mp_hand.HAND_CONNECTIONS)

            for id,landMrk in enumerate(hand_landmrk.landmark):
                print(f'details of each hand:\n'\
                    f'id : {id}\n{landMrk}')
                
                #dimensions of image feed with height and width
                height_img,width_img,channel_img = image.shape

                #finding position of center on image
                center_x,center_y = int(landMrk.x*width_img), int(landMrk.y*height_img)

                print(f'Dimensions of image in terms of pixels:\n'\
                    f'id:{id}\n'\
                    f'{center_x}\n{center_y}')

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





