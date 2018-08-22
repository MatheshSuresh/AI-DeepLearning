import cv2
import numpy as np
 
# read image into matrix.
m =  cv2.imread("1.jpg")
 
# get image properties.
h,w,bpp = np.shape(m)
 
# print image properties.
print ("width: " + str(w))
print ("height: " + str(h))
print ("bpp: " + str(bpp))
