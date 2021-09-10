import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])
    # Taking ranges br trial and error
    # Here trying for red color

    mask = cv2.inRange(hsv , lower_red , upper_red)
    # Creates a mask of every pixel that lies in that range
    res = cv2.bitwise_and(frame , frame , mask=mask)

    kernel = np.ones((5,5) , np.uint8)
    
    erosion = cv2.erode(mask , kernel , iterations=1)
##### EROSION #####
#  It erodes away the boundaries of foreground object.The kernel slides through the image (as in 2D convolution). A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
# All the pixels near boundary will be discarded depending upon the size of kernel. So the thickness or size of the foreground object decreases or simply white region decreases in the image. It is useful for removing small white noises, detach two connected objects etc.

    dilation = cv2.dilate(mask , kernel , iterations=1)
##### DILATION #####
# It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'. So it increases the white region in the image or size of foreground object increases. Normally, in cases like noise removal, erosion is followed by dilation. Because, erosion removes white noises, but it also shrinks our object. So we dilate it. Since noise is gone, they won't come back, but our object area increases. It is also useful in joining broken parts of an object.

    opening = cv2.morphologyEx(mask , cv2.MORPH_OPEN, kernel)
##### OPENING #####
# Opening is just another name of erosion followed by dilation. It is useful in removing noise. Here we use the function, cv.morphologyEx()

    closing = cv2.morphologyEx(mask , cv2.MORPH_CLOSE, kernel)
##### CLOSING #####
# Closing is reverse of Opening, Dilation followed by Erosion. It is useful in closing small holes inside the foreground objects, or small black points on the object.

##### MORE STUFF #####
#   # It is the difference between input image and Opening of the image
#     cv2.imshow('Tophat',tophat)

#     # It is the difference between the closing of the input image and input image.
#     cv2.imshow('Blackhat',blackhat)

    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    # cv2.imshow('erosion',erosion)
    # cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)



    k = cv2.waitKey(5) & 0xFF
    if k == 27: # 27 is escape key
        break

cv2.destroyAllWindows()
cv2.release()