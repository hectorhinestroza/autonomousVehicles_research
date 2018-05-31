import cv2
import numpy as np

"""def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),10,(10,45,143),-1)

img = np.zeros((300,300,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while (1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""

draw = False
mode = True
ix, iy = -1,-1

def draw_circle (event,x,y,flags,param):

    global draw,mode,ix,iy

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if draw is True:
            if mode is True:
                cv2.rectangle(img,(ix,iy),(x,y),(17,25,100),2)
            else:
                cv2.circle(img,(x,y),50,(100,56,32),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        if mode is True:
            cv2.rectangle(img, (ix, iy), (x, y), (17, 25, 100), 2)
        else:
            cv2.circle(img,(x,y),50, (100, 56, 32), -1)

img = np.zeros((500,500,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while (1):

    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break
    elif k == ord('m'):
        mode = not mode


cv2.destroyAllWindows()


