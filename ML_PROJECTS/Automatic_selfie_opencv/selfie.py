import cv2 
from random import randrange
camera_port =0
#capture the video on port 0
capture = cv2.VideoCapture(camera_port,cv2.CAP_DSHOW)

face_train = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#since a video is a set of continuous frames keep looping
while True:

    #capture each frame
    _, frame = capture.read()

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
    face_detect = face_train.detectMultiScale(grey_frames,1.3,5)

    #to display a border around a face that is detected

    for x_left_origin, y_left_origin,width_face,height_face in face_detect:

        #a rectangle to detect face
        # x_left_origin-> x top left corner
        # y_left_origin-> y top left corner
        # width_face-> horizontal width of face
        # height_face->vertical height of face
        # x_left_origin+width_face ,y_left_origin+height_face -> bottom right corner of rectangle
        cv2.rectangle(frame,(x_left_origin,y_left_origin),(x_left_origin+width_face,y_left_origin+height_face),(randrange(128,256),randrange(200,256),randrange(0,256)),5)
    cv2.imshow("face detector",frame)    
    #to exit from camera press "q"
    if cv2.waitKey(10) == ord('q'):
        break