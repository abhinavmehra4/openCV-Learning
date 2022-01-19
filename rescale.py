import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)


def rescaleFrame(frame,scale=0.2):
    #This method works for images, videos and live video
    width = int(frame.shape[1]*scale )#wight of the image
    height = int(frame.shape[0]*scale )#height of the image

    dimensions = (width,height) #a tuple of the dimensions are created

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) 

def changeRes(width,height):
    #works only for live videos, i.e from an external webcam or a laptop camera
    #below 3 references the width and 4 references the height.And that too by default.
    capture.set(3,width)
    capture.set(4,height)#if you want to change the brightness, then increase this to 10


resized_image = rescaleFrame(img)

cv.imshow('Image',resized_image) 

#Reading videos

capture = cv.VideoCapture('Videos/dog.mp4')#this method takes interger arguments or paths to a video file.

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = 0.2)

    #capture.read() reads the video frame by frame and retruns a boolean
    #isTrue to see if reading was successful
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
#to stop the video from playing indefinitely
    if cv.waitKey(20) & 0xFF==ord('d'):

     #if letter d is pressed, break out of the while loop   
        break

capture.release()
cv.destroyAllWindows()

"""
We use integers in case cameras are connected and integers from m0 to n are used to 
to refer to n cameras connected. For example, 0 refers to out
webcam and 1 to an external cam and so on..

But from a file path, integers aren't used, but paths are used
"""


