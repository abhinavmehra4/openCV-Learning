import cv2 as cv
import numpy as np
img = cv.imread('Photos/park.jpg')

cv.imshow('Park',img)

#1 Translation- shiting an image up down left right or any combination of these 4

def translate (img,  x,  y):
    #x corresponds to the number of pixels you want to shift to the x axis and y axis respectively
    transMat = np.float32([[1,0,x],[0,1,y]]) #in order to translate, we need to create a translation matrix
    dimensions = (img.shape[1],img.shape[0]) #shape[1] gets you the width anf shape[0] gets you the height.
    return cv.warpAffine(img,transMat,dimensions)

    # -x --------> shifting the image to the left
    # +x---------> shifting it to the right
    # +y---------> shifting it up
    # -y---------> shifting it down

translated = translate(img,100,100)

cv.imshow('Translated',translated)


cv.waitKey(0)
