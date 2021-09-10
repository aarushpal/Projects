import cv2
import numpy as np

img = cv2.imread('Images/bookpage.jpg')

retval, threshold = cv2.threshold(img , 12 ,255 , cv2.THRESH_BINARY)
grayscale = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
retval, threshold2 = cv2.threshold(grayscale , 12 ,255 , cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscale , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY , 115, 1)
# 1st param - passing in the blurred input image.
# 2nd param - the output threshold value, just as in simple thresholding and Otsu’s method.
# 3rd param - the adaptive thresholding method. Here we supply a value of cv2.ADAPTIVE_THRESH_MEAN_C to indicate that we are using the arithmetic mean of the local pixel neighborhood to compute our threshold value of T.
# We could also supply a value of cv2.ADAPTIVE_THRESH_GAUSSIAN_C (which we’ll do next) to indicate we want to use the Gaussian average — which method you choose is entirely dependent on our application and situation
# 4th param - the threshold method, again just like the simple thresholding and Otsu thresholding methods. Here we pass in a value of cv2.THRESH_BINARY_INV to indicate that any pixel value that passes the threshold test will have an output value of 0. Otherwise, it will have a value of 255.
# 5th param - our pixel neighborhood size. Here you can see that we’ll be computing the mean grayscale pixel intensity value of each 21×21 sub-region in the image to compute our threshold value T.
# 6th param - the constant C; this value simply lets us fine tune our threshold value.



cv2.imshow('original' ,  img)
cv2.imshow('threshold' ,  threshold)
cv2.imshow('threshold2' ,  threshold2)
cv2.imshow('gaus', gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()