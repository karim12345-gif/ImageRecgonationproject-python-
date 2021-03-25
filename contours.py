import cv2 as cv
import numpy as np
img = cv.imread('C:/Users/karim.salim/Desktop/car/poverty_india.jpg')
#shows the image
cv.imshow("preview", img)


gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)




cv.waitKey(0)