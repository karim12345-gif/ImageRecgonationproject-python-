import cv2 as cv 
import matplotlib.pyplot as plt
#import numpy as np 

image = cv.imread('C:/Users/karim.salim/Desktop/car/car1.jpg')
#shows the image
cv.imshow("Image", image)

#change to gray 
#gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)


#grayscale histogram 
#gray_hit= cv.calcHist([gray],[0],None,[256],[0,256])


#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hit)
#plt.xlim([0,256])
#splt.show()



#color histogram 
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([image],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])


plt.show()



cv.waitKey(0)


