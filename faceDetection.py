import cv2 as cv

#haar cascade are not used in advanced levels becuase they are not that accurate they are very senstive 


img = cv.imread('C:/Users/karim.salim/Desktop/car/group2.jpg')
#shows the image
cv.imshow("Image", img)


gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Gray person',gray)


#pass in the path of the harr_face XMl
#will read teh code and store it in the variable 
# haar_cascade are very senstive against the noise of the face so anything that looks like a face will be detected as 
#per ex lady gaga had many faces (nick , hiar and shirt ) that is expected from haar_cascade
#in order to solve the porblem, we have to minimize the senstivtie in scalefactgor and neighbors 
haar_cascade = cv.CascadeClassifier('haar_face.xml')


#detect faces change from 3 to 6 inorder to minimze the senstivetive of haar_cascade 
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1 , minNeighbors = 1)

#number of faces detected wwill be equal to 1 because theres only one person there 
print( f'number of faces found = {len(faces_rect)}')


#this draws the green rectangle around the persons face  and loops 
for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Dected faces',img)


cv.waitKey(0)


