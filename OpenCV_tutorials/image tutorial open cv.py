import cv2
#from matplotlib import pyplot as plt
import numpy as np


img = cv2.imread('img.jpg' ,1)
"""b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.imshow(img,interpolation='bicubic')
plt.show()
plt.imshow(img2,interpolation='bicubic')
plt.show()
"""
cv2.namedWindow('im', cv2.WINDOW_AUTOSIZE)
cv2.imshow('im',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



