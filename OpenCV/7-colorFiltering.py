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

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27: # 27 is escape key
        break

cv2.destroyAllWindows()
cv2.release()