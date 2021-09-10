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

    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)
    # The operation works like this: keep this kernel above a pixel, add all the 225 pixels below this kernel, take the average, and replace the central pixel with the new average value. This operation is continued for all the pixels in the image

    blur = cv2.GaussianBlur(res , (15,15), 0)
    median = cv2.medianBlur(res , 15)
    bilateral = cv2.bilateralFilter(res , 15, 75 ,75)

    cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    # cv2.imshow('smoothed' , smoothed)
    # cv2.imshow('blur' , blur)
    cv2.imshow('median' , median)
    cv2.imshow('bilateral' , bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: # 27 is escape key
        break

cv2.destroyAllWindows()
cv2.release()