

import cv2

#video file loaded
video_file = cv2.VideoCapture("ped_vid3.mp4")

# pretrained car classifier
car_classif = 'cars_trained.xml'
ped_classif = 'ped_trained.xml'


#training the model based on pretrained model
car_train = cv2.CascadeClassifier(car_classif)
ped_train = cv2.CascadeClassifier(ped_classif)
#read the video
while True:

    #read a single frame
    #returns whether if read is successful
    # And the video frame
    read_success,frame = video_file.read()

    #If we read the video properly convert it to black and white
    if read_success :
        #convert to grayscale
        gray_video = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #else just stop
    else:
        break

    #Detect the cars in the video
    cars_detect = car_train.detectMultiScale(gray_video,minNeighbors=3,scaleFactor = 1.02,minSize=[20,90])

    ped_detect = ped_train.detectMultiScale(gray_video,minNeighbors=3,scaleFactor = 1.03,minSize=[5,90])

    #weights = cars_detect[1]

    #we iterate over every frame and detect cars
    for (x,y,w,h) in cars_detect:
        cv2.rectangle(frame,(x,y),(w+x,y+h),(0,0,255),2)
        cv2.putText(frame,f'Vehicle' , (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    for (x,y,w,h) in ped_detect:
        cv2.rectangle(frame,(x,y),(w+x,y+h),(0,255,255),2)
        cv2.putText(frame,f'Person' , (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 2)
    
    #display image
    cv2.imshow("Car image",frame)
    cv2.waitKey(1)

print("\nProgram completed\n")



