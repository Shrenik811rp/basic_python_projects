# Using Haarcascade object detection algorithm to detect persons and cars
## Demo:
[demo of object detection](https://www.youtube.com/watch?v=c4LobbqeKZc)
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/c4LobbqeKZc/0.jpg)](http://www.youtube.com/watch?v=c4LobbqeKZc)

## End result:
![car_and_person_with_detection](https://buzzernepal.com/wp-content/uploads/2021/05/YOLOv3-for-Image-Detection.jpg)

Haarcascade can view an image and draw bounding over what it perceives as identified classes. We apply a single neural network to the full image. This network divedes the image into regions and predicts bounding boxes and probabilities for each region. These bounding boxes are weighted by the predicted probabilities. For more information about this algorithm, please, check [haarcascade](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html).

## Github repo for pretrained data:
### [Pretrained dataset](https://github.com/opencv/opencv/tree/master/data/haarcascades)

The haar-cascade cars.xml was trained using 526 images of cars from the rear (360 x 240 pixels, no scale). The images were extracted from the Car dataset proposed by Brad Philip and Paul Updike taken of the freeways of southern California.
## Installation: 
 
```python
!pip install 
```
-  Use the required dependencies in
### [reuirements.txt](https://github.com/Shrenik811rp/basic_python_projects/blob/master/ML_PROJECTS/FUN_AI_ML_PROJECTS/COMPUTER_VISION/OBJECT_DETECTION/CAR_PERSON_DETECT/requirements.txt)
## For more information, please see:

Train Your Own OpenCV Haar Classifier
- [opencv_haar](http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html)
- [github_data](https://github.com/mrnugget/opencv-haar-classifier-training)

## Related paper:

### Oliveira, M.; Santos, V. Automatic Detection of Cars in Real Roads using Haar-like Features (PDF)

Some additional resources:
- [car_rear_data](http://lars.mec.ua.pt/public/Media/ResearchDevelopmentProjects/HaarFeatures_RoadFilms/HaarFeaturesTests/CarsRear/)
- [research](http://lars.mec.ua.pt/public/Media/ResearchDevelopmentProjects/HaarFeatures_RoadFilms/HaarFeaturesTests/)
