import cv2
import numpy as np

img = np.empty((600,600,3), np.uint8)
img = cv2.line(img,(0,0),(599,599),(0,255,0),5)

img = cv2.rectangle(img,(390,0),(595,200),(255,0,0),5)

img = cv2.circle(img,(493,100),95,(0,0,255),-1)

img = cv2.ellipse(img,(300,300),(100,70),0,0,45,(0,0,255),-1)

pts = np.array([[50,0],[25,20],[38,50],[62,50],[75,20]], np.int32)
pts = pts.reshape((-1,1,2))

img = cv2.polylines(img,[pts],False,(255,255,255),3)
cv2.putText(img,'Open CV',(50,500),cv2.FONT_ITALIC,4,(255,0,0),4,cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.imwrite('img.jpg',img)


