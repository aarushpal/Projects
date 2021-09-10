import cv2
import numpy as np

img1 = cv2.imread('Images/3D-Matplotlib.png')
# img2 = cv2.imread('Images/mainsvmimage.png')
img2 = cv2.imread('Images/mainlogo.png')

##### Addition #####
# add = img1 + img2 # Retains each images' opacity
# add = cv2.add(img1 , img2) # Adds the corresponding pixel values

##### Weighted Addition #####
# weighted = cv2.addWeighted(img1 , 0.6 , img2 , 0.4 , 0)
# Adds images according to the weights specified
# last param is Gamma Value
# cv2.imshow('weighted' , weighted)

rows,cols,channels = img2.shape
roi = img1[0:rows , 0:cols]

img2grey = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)
ret , mask = cv2.threshold(img2grey , 220 ,255 , cv2.THRESH_BINARY_INV)
# THRESH_BINARY_INV converts any pixel value above 220 to black and lower than 220 to white
# cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
# Basically interchanges black and white values
# cv2.imshow('mask_inv', mask_inv)
img1_bg = cv2.bitwise_and(roi , roi , mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
# cv2.imshow('img1_bg', img1_bg)
# cv2.imshow('img2_fg', img2_fg)
dst = cv2.add(img1_bg , img2_fg)
img1[0:rows , 0:cols] = dst
cv2.imshow('res' , img1)


cv2.waitKey(0)
cv2.destroyAllWindows()