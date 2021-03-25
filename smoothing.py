import cv2 as cv
import numpy as np
img = cv.imread('C:/Users/karim.salim/Desktop/car/car1.jpg')
#shows the image
cv.imshow("preview", img)



#averaging 

average = cv.blur(img,(3,3))
cv.imshow('Averaging ',average)


#Glancing (less blur than the blur it self) if you increase the sigmax it gets more blury

gauss= cv.GaussianBlur(img ,(3,3),0)
cv.imshow('Gauss',gauss)


#median blur 
median = cv.medianBlur(img,(3))
cv.imshow('MEdian',median)



#bilater bluring 
bilater = cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilater',bilater)

cv.waitKey(0)