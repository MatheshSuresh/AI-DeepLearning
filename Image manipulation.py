import cv2
import numpy as np
 
# read image into matrix.
m =  cv2.imread("1.jpg") 
# get image properties.
h,w,bpp = np.shape(m)
 
# iterate over the entire image.
for py in range(0,h):
    for px in range(0,w):
        m[py][px][2] = 1
 
# display image
cv2.imshow('matrix', m)
cv2.waitKey(1)
