import cv2
import numpy as np

img = cv2.imread('sample.jpeg', cv2.IMREAD_COLOR) # Reading image
cv2.line(img , (0,0) , (150,150) , (255,255,255) , 15)
##### Drawing a line #####
# 1st param - where to draw a line
# 2nd param - starting coordinates of the line
# 3rd param - ending coordinates of the line
# 4th param - colour of line in bgr format
# 5th param - line width

cv2.rectangle(img , (200,200) , (400,400) , (0,255,0) ,10)
##### Drawing a rectangle #####
# 1st param - where to draw a line
# 2nd param - top left coordinates of the rectangle
# 3rd param - bottom right coordinates of the rectangle
# 4th param - colour of rectangle in bgr format
# 5th param - rectangle width

cv2.circle(img , (500,500) , 50 , (0,0,255) ,-1)
##### Drawing a circle #####
# 1st param - where to draw a circle
# 2nd param - centre coordinates
# 3rd param - radius
# 4th param - colour of circle
# 5th param - -1 indicates to fill the circle

pts = np.array([[10,5] ,[20,40] , [100,200] ,[60,80]] , np.int32)
cv2.polylines(img , [pts] , True , (255,0,255), 5)
##### Drawing a polygon #####
# 1st param - where to draw a polygon
# 2nd param - array of points
# 3rd param - whether last point should connect to the first point
# 4th param - colour of polygon
# 5th param - width

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img , 'Hello World', (800,400) ,font , 1 , (145,234,12), 2 , cv2.LINE_AA)
##### Drawing a polygon #####
# 1st param - where to write
# 2nd param - what to write
# 3rd param - starting coordinates
# 4th param - what font to use
# 5th param - size of text
# 6th param - color of text
# 7th param - spacing between the letters

cv2.imshow('image' , img)

cv2.waitKey(0)
cv2.destroyAllWindows