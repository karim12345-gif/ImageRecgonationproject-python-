import cv2 as cv 
import numpy as np 

blank = np.zeros((400,400),dtype='uint8')



rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('Circle',circle)




# biwsie AND

bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise_and',bitwise_and)

#bitwise or

bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or',bitwise_or)


#bitwise XOR

bitwise_XOR = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise_XOR',bitwise_XOR)


#bitwise not (it finds all the white image in rectangle and turns to them to black )

bitwise_not =- cv.bitwise_not(rectangle)
cv.imshow('bitwise_not',bitwise_not)


circle_not =- cv.bitwise_not(circle)
cv.imshow('circle_not',circle_not)




cv.waitKey(0)