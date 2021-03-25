import cv2 as cv
import numpy as np
#creating a blank image
imga = np.zeros([500,500,3], dtype=np.uint8)
cv.imshow('Blank',imga)

# 1 point the image a certain color(red color 0,0,255)
#imga [:] = 0,0,255
#cv.imshow('Green',imga)



#2.Draw a rectangle (green) using filled will make the whole rectangle green 
#cv.rectangle(imga,(0,0),(300,250),(0,222,0),thickness=cv.FILLED)
#cv.imshow('Rectnangle',imga)


#3. Draw a cricle 
#cv.circle(imga ,(250,250),40,(0,0,255),thickness=-1)
#cv.imshow('cricle=',imga)

#Draw a line 
cv.line(imga,(0,0),(250,250),(255,255,255),thickness=3)
cv.imshow('Line',imga)


# 4. Write a text on an image 

cv.putText(imga,'hello',(225,225),cv.FONT_HERSHEY_COMPLEX,1.0,(0,225,0),thickness=2)
cv.imshow('Text',imga)


cv.waitKey(0)
cv.destroyAllWindows()
