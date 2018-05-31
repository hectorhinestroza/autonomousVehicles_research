import cv2
import numpy as np
import imutils

#capture the video source (0) for camera or put the filename
cap = cv2.VideoCapture('motion.mp4')
# Show the images if connected to a display otherwise set to False
show_images = True


def main():
    while True:

        #read the video file frame by frame
        _,frame = cap.read()

        # resize the frame
        frame = imutils.resize(frame,height=500)
        """" color thresholding can be done with eiter BGR or HSV
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        lower = np.array([100,50,50])
        upper = np.array([130,255,255])
        """
        # set the color thresholds for grey color
        lower= np.array([75,75,75])
        upper = np.array([130,130,130])

        # use the inRange function to put white pixels between the set up range and black  everywhere else
        #mask = cv2.inRange(hsv,lower,upper)
        mask = cv2.inRange(frame,lower,upper)

        #use the bitwise function to combine the mask with it self using the mask (where the mask is white the frame its going to combine)
        #res = cv2.bitwise_and(frame,frame,mask = mask)
        res = cv2.bitwise_and(frame,frame,mask = mask)

        #blurr the picture using the medianBlur function
        blurred = cv2.medianBlur(res,5)

        #gScaled = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
        #threshold = cv2.adaptiveThreshold(gScaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,13,4)

        #detect the edges with the edge canny detector and draw all the contours found
        canny = cv2.Canny(blurred,70,130)
        vertices = np.array([[0,500],[0,350],[100,200],[181,200],[281,350],[281,500]])
        roi = region_of_interest(canny, vertices)

        (_, cnts, _) = cv2.findContours(roi.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame,cnts,-1,(0,255,0),1)

        #hough lines
        lines = cv2.HoughLines(roi,1,np.pi/180,180,np.array([]),30,10)
        #draw_lines(roi,lines)


        #loop over the contours to find those rectangular and big countours (like a road)
        """for c in cnts:
            approx = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
            arc =  (cv2.arcLength(c, True))
            if  arc > 20.0 and (len((approx)) > 4 and len((approx))) < 12: #cv2.contourArea(c) > 20 :
                cv2.drawContours(frame, [c], 0, (0, 0, 255), 1)
                #print (len(approx),cv2.contourArea(c))
        """

        # Show the images if connected to a display
        if show_images:
            cv2.imshow('blurred',blurred)
            cv2.imshow('bitwise function',res)
            cv2.imshow('inRange function',mask)
            #cv2.imshow('thresh',threshold)
            cv2.imshow('canny edge detector',canny)
            cv2.imshow('total result', frame)
            cv2.imshow('roi',roi)
            print (frame.shape)



        #cv2.imshow('tot',np.hstack([frame,mask,res,tot]))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

def region_of_interest (image,vertices):

    #blank mask
    mask = np.zeros_like(image)

    #fill the mask
    cv2.fillPoly(mask,[vertices],255)
    cv2.imshow('poly fil ', mask)

    #show only the are in the vertices
    masked = cv2.bitwise_and(image,mask)

    return masked

def draw_lines (image,lines):

    if lines:
        print ('succes')
        for line in lines:
            coord = line[0]
            cv2.line(image, (coord[0],coord[1]),(coord[2],coord[3]), [0,0,255],2)
        return True
    else:
        return False


if __name__ == '__main__':
    main()

