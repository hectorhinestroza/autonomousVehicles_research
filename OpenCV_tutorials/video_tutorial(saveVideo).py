import cv2
import numpy as np
import imutils
from imutils.video import VideoStream
import time

vs = VideoStream(usePiCamera= -1 > 0).start()
time.sleep(2.0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = None
(h,w) = (None, None)


while (1):

    frame = vs.read()
    frame = imutils.resize(frame,width=800)

    if writer is None:

        (h,w) = frame.shape[:2]
        writer = cv2.VideoWriter('2video.mp4',fourcc,30.0,(w,h),True)

    writer.write(frame)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
vs.stop()
writer.release()



