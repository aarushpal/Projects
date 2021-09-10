import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Images\img.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65) , np.float64)
fgdModel = np.zeros((1,65) , np.float64)

rect = (161,79,150,150)
# Hard-coded value according to the particular image used

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# img - Input image
# mask - It is a mask image where we specify which areas are background, foreground or probable background/foreground etc. It is done by the following flags, cv.GC_BGD, cv.GC_FGD, cv.GC_PR_BGD, cv.GC_PR_FGD, or simply pass 0,1,2,3 to image.
# rect - It is the coordinates of a rectangle which includes the foreground object in the format (x,y,w,h)
# bdgModel, fgdModel - These are arrays used by the algorithm internally. We just create two np.float64 type zero arrays of size (1,65).
# iterCount - Number of iterations the algorithm should run.
# mode - It should be cv.GC_INIT_WITH_RECT or cv.GC_INIT_WITH_MASK or combined which decides whether we are drawing rectangle or final touchup strokes.

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
# The mask is changed so that all 0 and 2 pixels are converted to the background, where the 1 and 3 pixels are now the foreground. From here, we multiply with the input image, and we get our final result

plt.imshow(img)
plt.colorbar()
plt.show()
