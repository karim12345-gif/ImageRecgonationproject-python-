import cv2 as cv
import numpy as np
img = cv.imread('C:/Users/karim.salim/Desktop/car/poverty_india.jpg')
#shows the image
cv.imshow("preview", img)

# uint 8 basically offers images
blank = np.zeros(img.shape[:2],dtype='uint8')



#b,g,r 
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)

cv.imshow('Green',green)

cv.imshow('Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


# mergering the 3 colors 

merge = cv.merge([b,g,r])
cv.imshow('Merge',merge)


cv.waitKey(0)