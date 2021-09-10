import cv2
import numpy as np

cap = cv2.VideoCapture(0) # Initializing video capture object
# 0 starts the first connected camera
fourcc = cv2.VideoWriter_fourcc(*'XVID') # Initializing codec
out = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640,480))
# 1st param - name of the video saved
# 2nd param - codec used
# 3rd param - frame rate
# 4th param - size of the saved video
while True:
    ret , frame = cap.read()
    cv2.imshow('frame' , frame)
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'): # Checks if a key is pressed and it is 'q'
        break

cap.release() # Releases the webcam
out.release()
cv2.destroyAllWindows()