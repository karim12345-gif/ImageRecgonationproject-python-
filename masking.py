import cv2 as cv 
import numpy as np 

img = cv.imread('C:/Users/karim.salim/Desktop/car/poverty_india.jpg')
#shows the image
cv.imshow("Image", img)
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank image',blank)
# adding values (pixles ) can move the circle 
mask= cv.circle(blank,(img.shape[1]//2 +25 ,img.shape[0]//2 +25),100,255,-1)
cv.imshow('MAsk',mask)


#apply the picture inside the white circle from the mask 
masked= cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked',masked)

cv.waitKey(0)