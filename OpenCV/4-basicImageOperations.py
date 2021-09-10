import cv2
import numpy as np

img = cv2.imread('sample.jpeg' , cv2.IMREAD_COLOR)

# px = img[55,55] # Returns the color value the pixel
# print(px)

# ## Region of Interest/Image ##
# px = img[100:200 , 300:400] # returns color values of the region specified
# print(px) 

## Converting roi to some color ##
img[100:200 , 200:400] = [255,255,255] # converting that region to white rectangle
cv2.imshow('image' , img)

## Copy Paste a part of image to another region ##
# crop = img[500:600 , 600:800]
# img[0:100 , 0:200] = crop

cv2.waitKey(0)
cv2.destroyAllWindows()