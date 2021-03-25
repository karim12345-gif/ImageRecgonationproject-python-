import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('C:/Users/karim.salim/Desktop/car/poverty_india.jpg')
#shows the image
cv.imshow("preview", img)

plt.imshow(img)
plt.show()



# convert to gray scale 

#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray image',gray)


# BGR to HSV


hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV image',hsv)


#BGR to l*a*b 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab image',lab)


#HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr',hsv_bgr)

#lab to BGR
lab_bgr = cv.cvtColor(lab,cv.COLOR_HSV2BGR)
cv.imshow('lab_bgr',lab_bgr)



cv.waitKey(0)