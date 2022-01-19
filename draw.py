#Drawing on an image can be done by doing it actually on an image or creating a dummy image.

import numpy as np
import cv2 as cv

blank = np.zeros((500,500,3), dtype = 'uint8' ) # 500, 500,3 corresponds to the height width and the number of color channels respectively.

#uint8 is the datatype of an image.
cv.imshow('Blank', blank)

# #1. Painting the image

# blank[200:300, 300:400]=0,0,255 #In this a range of pixels get coloured. But if you want the entire image to be coloured, then select all of the pixels by using [:] slicing technique
# cv.imshow('Green', blank)
#all the pixels in blank are referred to 

#2 Drawing a rectangle

cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=cv.FILLED)
#cv.rectangle(img, pt1, pt2, color, thickness=..., lineType=..., shift=...)
#What to do if you want to fill the rectangle created above? 
#cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=cv.FILLED)
#Or, it can also be done by, "cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=-1)"

#We can also make a rectangle of 250x250 using the following
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[1]//2),(0,250,0),thickness=-1)
#In the above case, the dimensions of the actual image have been reduced to half of the original size
cv.imshow('Rectangle',blank)  

#3 Drawing a circle

cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
#similarly, to fill the circle and draw it, one could do what they did with the rectangle
#cv.circle(blank,(blank.shape[1]//2,blank.shape[1]//2),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank) 


#4 drawing a line

cv.line(blank,(100,250),(300,400),(255,250,255),thickness=3)
#no need to use the shape function because for drawing a line, no need to resize her. Instead ewe are using the coordinates of the start and end of the line.
cv.imshow('Line',blank)


#5 Writing a text on an image

cv.putText(blank,'Hello Bitches, I am back motherfuckers',(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness =2)
cv.imshow('Text',blank )
cv.waitKey(0)
 
