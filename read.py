import cv2 as cv

#img = cv.imread('Photos/cat_large.jpg')#stores the pixels of this image in a matrix 

#cv.imshow('Cat',img)#name of the window and matrix of pixels you want to display
#cv.waitKey(0) #It waits for an infinite amount of time for a keyboard to be pressed. This is when '0' is put inside the brackets.

#Reading videos

capture = cv.VideoCapture('Videos/dog.mp4')#this method takes interger arguments or paths to a video file. VideoCapture is a class with many methods inside it that we dont know of yet.


while True:
    isTrue, frame = capture.read()

    #capture.read() reads the video frame by frame and retruns a boolean
    #isTrue to see if reading was successful
    cv.imshow('Video',frame)

#to stop the video from playing indefinitely
    if cv.waitKey(20) & 0xFF==ord('d'):

     #if letter d is pressed, break out of the while loop   
        break

capture.release()
cv.destroyAllWindows()

"""
We use integers in case cameras are connected and integers from 0 to n are used to 
to refer to n cameras connected. For example, 0 refers to our
webcam and 1 to an external cam and so on..

But from a file path, integers aren't used, but paths are used
"""


