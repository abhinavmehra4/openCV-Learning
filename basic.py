import cv2 as cv
img = cv.imread('Photos/park.jpg')
cv.imshow('PARK',img)
#1 Converting an image to grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Gray',gray)

#2 Blur

blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
#the tuple (3,3) can be anything. It is a kernel but it has to be an odd value. It is the image size.
#INCREASE THE KERNAL SIZE TO INCREASE THE BLUR


#3 Edge Cascade

canny = cv.Canny(img,125,175)
cv.imshow('Canny Image', canny)
#to reduce the number of edges we can blur the image.
# canny = cv.Canny(blur,125,175)
# cv.imshow('Canny Image', canny)


#4 Dilating an image

#this requires passing the structuring element which in this case is the canny that we have created above.
#The edge lines get thicker and thicker
dilated = cv.dilate(canny,(7,7),iterations = 3)
cv.imshow('Dilated',dilated)

#5 Eroding- we get the canny edge image back from a dilated image.
#i.e we need to pass the 'dilated' image to get back the image with think edges

eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#structuring element(canny edge image) ------> diluted image ----------> eroded image
#                                      <------               <---------

#6 Resizing an image

resized = cv.resize(img,(500,500), interpolation = cv.INTER_AREA)#this is used when you have to reduce the size
#but in case youii want to scale the image to a much mich bigger sze you can us e the following
#interpolation = cv.INTER_CUBIC or interpolation = cv.INTER_LINEAR

cv.imshow('Resized',resized)

#Cropping an image
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)


cv.waitKey(0)

