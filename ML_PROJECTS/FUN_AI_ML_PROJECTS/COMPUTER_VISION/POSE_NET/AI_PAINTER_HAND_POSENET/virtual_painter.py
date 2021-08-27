import cv2
import numpy as np
import os
import time
import hand_track_module as htm


brushThickness = 15
eraserThickness = 100
#default draw set at 0,0
index_prev_y = 0
index_prev_x = 0

#create a separate canvas to draw with dimensions 720,1280
# we want colors of rgb from 0 to 255
# so 3 ->RGB uint8 - >0-255
imageCanvas = np.zeros((720,1280,3),np.uint8) + 255

folder_path = "images"
my_img_list = os.listdir(folder_path)
print(my_img_list)

overlay_list = []
for image_path in my_img_list:
    image = cv2.imread(f'{folder_path}/{image_path}')
    overlay_list.append(image)

print(len(overlay_list))

header = overlay_list[0]

draw_color = (0, 128, 248)

capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)

capture.set(3,1280)
capture.set(4,720)

detector = htm.hand_detector_func(detectConf=0.9)

while True:
    result, image = capture.read()
    #flip image to avoid confusion while drawing

    image = cv2.flip(image,1)

    #1.Find landmarks

    image = detector.findHands(image)

    #get landmark list
    landmark_list = detector.findPosition(image,draw=False)

    if len(landmark_list) != 0:
        #print(landmark_list)

        #tip of index and middle finger
        # We get only the x and y coordinates not the id so [1:0]
        index_fing_x,index_fing_y = landmark_list[8][1:]
        middle_fing_x,middle_fing_y = landmark_list[12][1:]

        # 3. Check which fingers are up
        #check which finger is up
        fingers = detector.fingerUp()
        print(fingers)


        # 4. Selection mode
        # when index 1 and 2 are "1"
        # index and middle finger
        if fingers[1] and fingers[2]:
            index_prev_y = 0
            index_prev_x = 0
            print("Select")

            if index_fing_y < 125:
                if 150 < index_fing_x < 340:
                    header = overlay_list[0]
                    draw_color =(204, 0, 102)
                elif 350 < index_fing_x < 485:
                    header = overlay_list[1]
                    draw_color =(0, 0, 255)
                elif 495 < index_fing_x < 600:
                    header = overlay_list[2]
                    draw_color =(127, 0, 255)
                elif 610 < index_fing_x < 740:
                    header = overlay_list[3]
                    draw_color =(0, 0, 0)
                elif 750 < index_fing_x < 880:
                    header = overlay_list[4] 
                    draw_color =(0, 153, 0)
                elif 890 < index_fing_x < 1010:
                    header = overlay_list[5]
                    draw_color =(255, 255,0)
                elif 1020 < index_fing_x < 1150:
                    header = overlay_list[6]
                    draw_color =(255, 255, 255)  
            cv2.rectangle(image,(index_fing_x,index_fing_y-30),(middle_fing_x,middle_fing_y+30),draw_color,cv2.FILLED)     


        # 5. Drawing mode
        # only index finger 
        # index 1 is high
        if fingers[1] and fingers[2] == False:
            cv2.circle(image,(index_fing_x,index_fing_y),15,draw_color,cv2.FILLED)
            print("Draw")

            # to prevent drawing a line at very first iteration from origin to where finger is by default
            if index_prev_x == 0 and index_prev_y == 0:
                index_prev_x,index_prev_y = index_fing_x,index_fing_y
            
            if draw_color == (255,255,255):
                #drawing line
                cv2.line(image,(index_prev_x,index_prev_y),(index_fing_x,index_fing_y),draw_color,eraserThickness)
                #canvas
                cv2.line(imageCanvas,(index_prev_x,index_prev_y),(index_fing_x,index_fing_y),draw_color,eraserThickness)
            else:
                cv2.line(image,(index_prev_x,index_prev_y),(index_fing_x,index_fing_y),draw_color,brushThickness)
                #canvas
                cv2.line(imageCanvas,(index_prev_x,index_prev_y),(index_fing_x,index_fing_y),draw_color,brushThickness)    



            # updating x and y coordinates
            index_prev_x,index_prev_y = index_fing_x,index_fing_y


    #overlaying selection bar on top of video
    image[0:125,0:1280] = header

    #merging canvas and video feed
    image = cv2.addWeighted(image,0.5,imageCanvas,0.5,0)

    cv2.imshow("Hand tracking",image)
    #cv2.imshow("Canvas",imageCanvas)
    #to quit press "q" wait for 10 sec
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# closes the window
capture.release()

# destroy or close the gui window
cv2.destroyAllWindows()
print("window closed")

