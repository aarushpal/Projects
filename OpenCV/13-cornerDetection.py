import cv2
import numpy as np

img = cv2.imread('Images\opencv-corner-detection-sample.jpg')
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

# cv.goodFeaturesToTrack() finds N strongest corners in the image by Shi-Tomasi method. Image should be a grayscale image. 
# 1st param - image to detect corners
# 2nd param - number of corners we want to find.
# 3rd param - quality level, which is a value between 0-1, which denotes the minimum quality of corner below which everyone is rejected
# 4th param - the minimum euclidean distance between corners detected

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    
cv2.imshow('Corner',img)