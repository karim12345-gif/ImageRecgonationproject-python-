import cv2 as cv
import numpy as np
img = cv.imread('car/car detector.jpg')
#shows the image
cv.imshow("preview", img)


def translate(img , x, y):
    transMat = np.float32([1,0,x],[0,1,y])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)



# x is left and right horizontal 
# y is vertical so up and down 

translated = translate(img,-100,100)
cv.imshow('Translated',translated)
