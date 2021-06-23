import cv2 
from random import randrange

camera_port =0
#capture the video on port 0
capture = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)

#trains on face images and pretrained model to detect faces
face_train = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#variable that stores pretrained model that detects smiles from haarcascade
smile_train = cv2.CascadeClassifier('haarcascade_smile.xml')

#since a video is a set of continuous frames keep looping
while True:

    #capture each frame
    _, frame = capture.read()

    #to remove border frames to detect face and smile

    frame_without_border = frame.copy()

    #detect a face turn color into grey

    # convert the video from source which is "frame" and use cv2 method to change video into grey image
    grey_frames = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #show video displayed
    #uncomment this line to see
    #cv2.imshow("camera start",frame)

    #to show grey image of video
    #uncomment this line to see
    #cv2.imshow('grey video start',grey_frames)

    #code that will detect face using pretrained data model stored in face_train

    #detect face from grey video not from color video
    #number of multiscales set to 1.3
    #max boundries to detect face set to 5
    face_detect = face_train.detectMultiScale(grey_frames,1.4,3)

    #to display a border around a face that is detected

    for x_left_origin, y_left_origin,width_face,height_face in face_detect:

        #a rectangle to detect face
        # x_left_origin-> x top left corner
        # y_left_origin-> y top left corner
        # width_face-> horizontal width of face
        # height_face->vertical height of face
        # x_left_origin+width_face ,y_left_origin+height_face -> bottom right corner of rectangle
        cv2.rectangle(frame,(x_left_origin,y_left_origin),(x_left_origin+width_face,y_left_origin+height_face),(255,0,0),2)


        #since smile will be always inside or within face 

        #face_roi shows area where one should focus on to get a smile

        #so to focus only on face start from origin upto width and height of a persons face
        face_roi = frame[y_left_origin:y_left_origin+ height_face,x_left_origin:x_left_origin+width_face]

        #to use the greyimage version of video
        #to focus on face where we will detect our smile of that person
        grey_roi = grey_frames[y_left_origin:y_left_origin+ height_face,x_left_origin:x_left_origin+width_face]

        #to ddetect smile use the similar process to detect a face
        #we detect the smile based on black and white video as it is easier to process
        smile_detect = smile_train.detectMultiScale(grey_roi,1.8,25)

        #now to draw a rectangle when smile is detected do a for loop based on coordinates similar to face
        for x_left_smile,y_left_smile,smile_width,smile_height in smile_detect:

            #we draw on color video and use grey video to detect smile
            cv2.rectangle(face_roi,(x_left_smile,y_left_origin),(x_left_smile+smile_width,y_left_origin+smile_height),(0,0,255),2)

            #to get selfie image of smile 
            cv2.imwrite("my_selfie.png",frame_without_border)
    cv2.imshow("face detector",frame)    
    #to exit from camera press "q"
    if cv2.waitKey(10) == ord('q'):
        break