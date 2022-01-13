import time
start = time.time()
import cv2 as cv

videos = ['Videos/kitten.mp4', 'Videos/dog.mp4']

for i in range(0,len(videos)):

    capture = cv.VideoCapture(videos[i])

    while True:
        isTrue, frame = capture.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('