import numpy as np 
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['elton johns','harry','mohamed salah','zayn']

#loading both of them 
features = np.load('features.npy')
labels = np.load('labels.npy')


faces_recognizer = cv.face.LBPHFaceRecognizer_create()
faces_recognizer.read('face_trained.yml')


img= cv.imread(r'C:/Users/karim.salim\Desktop/faces/trains/harry/harry1.jpg')


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",img)


#detect the face image 

faces_rect =haar_cascade.detectMultiScale(gray, scaleFactor = 1.1 , minNeighbors = 4)

for (x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+h]


    label, confidence = faces_recognizer.predict(faces_roi)

