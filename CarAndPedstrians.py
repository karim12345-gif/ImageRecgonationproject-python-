import cv2

img = cv2.imread('C:/Users/karim.salim/Desktop/car/poverty_india.jpg' ,0)
#shows the image

cv2.imshow("preview", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
