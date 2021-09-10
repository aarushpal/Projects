from PIL.Image import BICUBIC
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sample.jpeg', cv2.IMREAD_GRAYSCALE) # Reads the image in greyscale
cv2.imshow('image', img) 
# 1st param takes the title of the display window
# 2nd param takes the image 
cv2.waitKey(0) # Waits for any key to be pressed
cv2.destroyAllWindows() # Closes the window 

##### DISPLAYING WITH MATPLOTLIB #####
# plt.imshow(img , cmap='gray')
# plt.show()

##### SAVING IMAGE #####
# cv2.imwrite('newsample.jpg', img)
