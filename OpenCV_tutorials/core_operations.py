import cv2
import numpy as np

#image addition and blending
"""img = cv2.imread('img.jpg',1)
img1 = cv2.imread('stop.png')

#added = cv2.addWeighted(img,0.2,img1,0.8,0)
added = cv2.add(img,img1)
cv2.imshow('img',added)
cv2.waitKey(0)
cv2.destroyAllWindows()

px = img[100,100]
blue = img[100,100,1]
img.item(10,10,2)

#print (px)
#print (blue)
"""

#Bitwise Operations

img = cv2.imread('image.jpg')
img1 = cv2.imread('logo.png')

# I want to put logo on top-left corner, So I create a ROI

rows, cols, channels = img1.shape
roi = img[0:rows,0:cols]

# Now create a mask of logo and create its inverse mask also
img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

cv2.imshow('img1_gray',img1_gray)
cv2.waitKey(0)


mask1 = cv2.bitwise_not(img1_gray)

cv2.imshow('mask1',mask1)
cv2.waitKey(0)



ret, mask = cv2.threshold(mask1,10,255,cv2.THRESH_BINARY)

cv2.imshow('mask',mask)
cv2.waitKey(0)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)
cv2.waitKey(0)


# Now black-out the area of logo in ROI
img_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('img_bg',img_bg)
cv2.waitKey(0)


# Take only region of logo from logo image.

img1_fg = cv2.bitwise_and(img1,img1,mask = mask)
cv2.imshow('img1_fg',img1_fg)
cv2.waitKey(0)


# Put logo in ROI and modify the main image

dst = cv2.add(img_bg,img1_fg)
img[0:rows,0:cols] = dst

cv2.imshow('res',img)
cv2.waitKey(0)
cv2.destroyAllWindows()





