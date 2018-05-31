from imutils.video import VideoStream
import imutils
import cv2
import numpy as np
import time

# initialize the video stream and allow the camera
# sensor to warmup

vs = VideoStream(usePiCamera = -1 > 0).start()
time.sleep(2.0)

# initialize the FourCC, video writer, dimensions of the frame, and
# zeros array

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = None
(h,w) = (None,None)
zeros = None



# loop over frames from the video stream

while(1):

    frame = vs.read()
    frame = imutils.resize(frame,width=300)

    if writer is None :
        #store the image dimensions, initialize the video writer
        #and construct zero array
        (h,w) = frame.shape[:2]
        writer = cv2.VideoWriter('video.mp4', fourcc, 30.0, (w * 2, h * 2),True)
        zeros = np.zeros((h,w), dtype="uint8")

    (B, G, R) = cv2.split(frame)
    R = cv2.merge([zeros, zeros, R])
    G = cv2.merge([zeros, G, zeros])
    B = cv2.merge([B, zeros, zeros])

    # construct the final output frame, storing the original frame
    # at the top-left, the red channel in the top-right, the green
    # channel in the bottom-right, and the blue channel in the
    # bottom-left
    output = np.zeros((h * 2, w * 2, 3), dtype="uint8")
    output[0:h, 0:w] = frame
    output[0:h, w:w * 2] = R
    output[h:h * 2, w:w * 2] = G
    output[h:h * 2, 0:w] = B

    # write the output frame to file
    writer.write(output)

    cv2.imshow('frame', frame)
    cv2.imshow('output', output)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
vs.stop()
writer.release()





