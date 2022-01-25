import cv2
import numpy as np
from skylearn.metrics import pairwise

cap = cv2.VideoCapture(0)
#if jiggers are present other that yellow area
kernelOpen = np.ones((5,5))
#if jiggers are present in yellow area
kernelClose = np.ones((20,20))
#HSV color range which should be detected
lb = np.array([20,100,100])
ub = np.array([120,255,255])

while True:
    ret, frame = cap.read()
    flipped = cv2.flip(frame, 1)
    flipped = cv2.resize(flipped, (500,400))

    #use HSV of yellow to detect only yellow color
    imgSeg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    imgSegFlipped = cv2.flip(imgSeg, 1)
    imgSegFlipped = cv2.resize(imgSegFlipped,(500,400))

    #masking and filtering all shades of yellow
    mask = cv2.inRange(imgSegFlipped,lb,ub)
    mask = cv2.resize(mask,(500,400))

    #apply morphology to avoid jiggers
    maskOpen = cv2.morphologyEx()