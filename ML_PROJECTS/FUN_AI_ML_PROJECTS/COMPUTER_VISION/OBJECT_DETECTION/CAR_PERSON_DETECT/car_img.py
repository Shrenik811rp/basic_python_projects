

import cv2

#image loaded
img_file = 'img2.jpg'

# pretrained car classifier
car_classif = 'cars_trained.xml'

#read the image
img = cv2.imread(img_file)

#convert image from color to black and white
black_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#create car classifier
car_train = cv2.CascadeClassifier(car_classif)

#detect the car in the image
# And display the coordinates of the car
car_detect = car_train.detectMultiScale(black_img)

print(f'Car coordinates: {car_detect}\n')

for (x,y,w,h) in car_detect:
    cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),2)


#display image
cv2.imshow("Car image",img)

cv2.waitKey(10000)

print("\nProgram completed\n")




