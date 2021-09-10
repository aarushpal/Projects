import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame , cv2.CV_64F)

##### LAPLACIAN OPERATOR #####  
# It is an edge detector used to compute the second derivatives of an image, measuring the rate at which the first derivatives change. This determines if a change in adjacent pixel values is from an edge or continuous progression.
# Laplacian filter kernels usually contain negative values in a cross pattern, centered within the array. The corners are either zero or positive values. The center value can be either negative or positive.

    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)

##### SOBEL FILTER #####
# It detects edges that are marked by sudden changes in pixel intensity. The Sobel Operator detects edges that are marked by sudden changes in pixel intensity. We can approximate the derivative, using a 3×3 kernel. We use one kernel to detect sudden changes in pixel intensity in the X direction, and another in the Y direction.If we use only the Vertical Kernel, the convolution yields a Sobel image, with edges enhanced in the X-direction. Using the Horizontal Kernel yields a Sobel image, with edges enhanced in the Y-direction. 

    edges = cv2.Canny(frame,100,200)
    
##### CANNY EDGE DETECTION #####

# STEP 1 -  Noise Reduction
# First step is to remove the noise in the image with a 5x5 Gaussian filter.

# STEP 2 - Finding Intensity Gradient of the Image
# Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction to get first derivative in horizontal direction ( Gx) and vertical direction ( Gy). From these two images, we can find edge gradient and direction for each pixel as follows:
# Edge_Gradient(G)=G2x+G2y−−−−−−−√Angle(θ)=tan−1(GyGx)

# STEP 3 - Non-maximum Suppression
# After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels which may not constitute the edge. For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient.
# In short, the result you get is a binary image with "thin edges".

# STEP 4 -  Hysteresis Thresholding
# This stage decides which are all edges are really edges and which are not. For this, we need two threshold values, minVal and maxVal. Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. If they are connected to "sure-edge" pixels, they are considered to be part of edges. Otherwise, they are also discarded. 

    cv2.imshow('original' , frame)
    cv2.imshow('laplacian' , laplacian)
    cv2.imshow('sobelx' , sobelx)
    cv2.imshow('sobely' , sobely)
    cv2.imshow('Edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: # 27 is escape key
        break

cv2.destroyAllWindows()
cv2.release()