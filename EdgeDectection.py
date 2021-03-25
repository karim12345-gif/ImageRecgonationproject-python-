import cv2 as cv 
import numpy as np 

img = cv.imread('C:/Users/karim.salim/Desktop/car/poverty_india.jpg')
#shows the image
cv.imshow("Image", img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)



#laplaction(not used that much )
lap= cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lapaction',lap)


#sobel ( only used in advanced cases)
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)


cv.imshow('SobelX',sobelx)
cv.imshow('sobelY',sobely)
cv.imshow('Combine_sobel_OR',combined_sobel)



#canny(used more often because its clearner )
canny = cv.Canny(gray,150,175)
cv.imshow('canny',canny)

cv.waitKey(0)