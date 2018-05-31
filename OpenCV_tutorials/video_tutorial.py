import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter()
success = out.open('output.mp4',fourcc,20.0,(1280,800),True)

while(cap.isOpened()):

    ret, frame = cap.read()

    if ret==True:
        frame = cv2.flip(frame,0)

        out.write(frame)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('k'):
            break
    else:
        break


"""while(1) :

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('c') :
        break
"""


cap.release()
out.release()
cv2.destroyAllWindows()






