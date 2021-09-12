

#importing required dependencies

import tensorflow as tf
import tensorflow_hub as hub 
import cv2
from matplotlib import pyplot as plt
import numpy as np


#load model
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')


#give image path
def load_image(img_path):
  #read image file
  img = tf.io.read_file(img_path)
  # passing image
  img = tf.image.decode_image(img,channels=3)

  #formatting image
  img = tf.image.convert_image_dtype(img,tf.float32)

  #image is in an array
  img = img[tf.newaxis,:]
  return img



#content_img is the main image
content_image = load_image('/content/Koala.jpg')

#style image is the image we overlap
style_image = load_image('/content/painting2.jpg')

#display image
plt.imshow(np.squeeze(content_image))
plt.show()

#image dimensions
content_image.shape

#display image
plt.imshow(np.squeeze(style_image))
plt.show()

#combine both the image and the painting
combined_image = model(tf.constant(content_image), tf.constant(style_image))[0]

#display image
plt.imshow(np.squeeze(combined_image))
plt.show()


#export combined product as image jpg
cv2.imwrite('combined_img.jpg', cv2.cvtColor(np.squeeze(combined_image)*255, cv2.COLOR_BGR2RGB))
