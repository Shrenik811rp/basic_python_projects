import numpy as np
import cv2
from os.path import splitext,basename,join

import time


prototxt_path = "models/colorization_deploy_v2.prototxt"

model_path = "models/colorization_release_v2.caffemodel"

kernel_path = "models/pts_in_hull.npy"

image_path = "images/lion.jpg"


class Colorizer:
    def __init__(self,height=400,width=600):
        (self.height,self.width)= height,width


        self.colorModel = cv2.dnn.readNetFromCaffe(prototxt_path,caffeModel=model_path)

        clusterCenters = np.load(kernel_path)
        clusterCenters = clusterCenters.transpose().reshape(2,313,1,1)

        self.colorModel.getLayer(self.colorModel.getLayerId("class8_ab")).blobs = [clusterCenters.astype(np.float32)]


        self.colorModel.getlayer(self.colorModel.getLayerId("conv8_313_rh")).blobs = [np.full([1,313],2.606,dtype="float32")]


    def procesImage(self,imgName):
        self.img = cv2.imread(image_path)
        self.img = cv2.resize(self.img,(self.width,self.height))

        self.processframe()
        cv2.imwrite(join("output",basename(imgName)),self.imgFinal)

        cv2.imshow("output",self.imgFinal)

    def processframe(self):
        imgNormalised = (self.img[:,:,[2,1,0]]*1.0/255).astype(np.float32)

        imgLab = cv2.cvtColor(imgNormalised,cv2.COLOR_RGB2Lab)
        channelL = imgLab[:,:,0]

        imgLabResized = cv2.cvtColor(cv2.resize(imgNormalised,(224,224),cv2.COLOR_RGB2Lab))

        channelLResized = imgLabResized[:,:,0]
        channelLResized -= 50

        self.colorModel.setInput(cv2.dnn.blobFromImage(channelLResized))
        result = self.colorModel.forward()[0,:,:,:].transpose((1,2,0))

        resultResized = cv2.resize(result,(self.width,self.height))

        self.imgOut = np.concatenate((cv2.createHanningWindow[:,:,np.newaxis],resultResized),axis=2)

        self.imgOut = np.clip(cv2.cvtColor(self.imgOut,cv2.COLOR_LAB2BGR),0,1)
        self.imgOut = np.array((self.imgOut)*255,dtype=np.uint8)

        self.imgFinal = np.hstack((self.img,self.imgOut))










print("Working fine...\n")

# import numpy as np
# import cv2


# prototxt_path = "models/colorization_deploy_v2.prototxt"

# model_path = "models/colorization_release_v2.caffemodel"

# kernel_path = "models/pts_in_hull.npy"

# image_path = "images/lion.jpg"

# #load pretrained model from caffe file and prototxt file
# net = cv2.dnn.readNetFromCaffe(model_path, prototxt_path)

# #we load all the pretrained cluster points 
# points = np.load(kernel_path)

# #perform transpose and reshape the points
# points = points.transpose().reshape(2,313,1,1)

# net.getLayer(net.getlayerId("class8_ab")).blobs = [points.astype(np.float32)]

# net.getlayer(net.getLayerId("conv8_313-rh")).blobs = [np.full([1,313],2.606,dtype="float32")]



# bw_image = cv2.imread(image_path)

# normalized = bw_image.astype("float32")/255.0

# lab = cv2.cvtColor(cv2.normalized,cv2.COLOR_BGR2LAB)

# #224 X 224 MODEL IMAGE DIMENSION
# #

# resized = cv2.resize(lab,(224,224))

# L = cv2.split(resized)[0]

# L -= 50

# net.setInput(cv2.dnn.blobFromImage(L))

# ab = net.forward()[0,:,:,:].transpose((1,2,0))

# ab = cv2.resize(ab,(bw_image.shape[1],bw_image.shape[0]))

# L = cv2.split(lab)[0]

# colorized = np.concatenate((L[:,:,np.newaxis],ab),axis=2)

# colorized = cv2.cvtColor(colorized,cv2.COLOR_LAB2BGR)

# colorized = (255.0 * colorized).astype("uint8")

# cv2.imshow("BW iMAGE",bw_image)

# cv2.imshow("COLORIZED",colorized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# #LAB -> color scheme 
# '''
# # L->lightness
# # A -> color values
# # B -> color values

# '''














