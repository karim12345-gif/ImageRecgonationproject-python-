import cv2 as cv
img = cv.imread('C:/Users/karim.salim/Desktop/car/car1.jpg')
#shows the image
cv.imshow("preview", img)

# 1-convert to grayScale
#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

#2-Blur image the KSize always has to be an odd number (makes the image blury and not clear)
#blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)


#Edge Cascade detector (find the edges in the image )
#canny = cv.Canny(blur,125,175)
#cv.imshow('canny edges',canny)


# 4- dilating image way thicker than the canny image becuase of the iterations 
#dilated = cv.dilate(canny,(7,7),iterations=3)
#cv.imshow("dilated image",dilated)



#5-Eroding is what u get from both dilated and cascade or canny 
#eroded = cv.erode(dilated,(7,7),iterations=3)
#cv.imshow("Eroded image",eroded)



# 6- resize and image makes it bigger or smaller up to u , Inter_Cubic is the best quality 
#Resize = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
#cv.imshow("Resize",Resize)


#7-cropping or slicing images
cropping = img[50:200,200:400]
cv.imshow("cropped",cropping)


cv.waitKey(0)
cv.destroyAllWindows()
