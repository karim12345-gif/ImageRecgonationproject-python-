import os 
import cv2 as cv 
import numpy as np 


people = ['elton johns','harry','mohamed salah','zayn']

DIR = r'C:\Users\karim.salim\Desktop\faces\trains'

haar_cascade = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []



def create_train():
    #we are going to loop over each person 
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)
        #now we are inside each folder in people 


        for img in os.listdir(path):
            #grab image path 
            img_path = os.path.join(path,img)
            #to read the image 
            im_array = cv.imread(img_path)
            #covnert to gray 
            gray = cv.cvtColor(im_array,cv.COLOR_BGR2GRAY)

            #detect the faces 
            faces_rect =haar_cascade.detectMultiScale(gray, scaleFactor = 1.1 , minNeighbors = 4)
             


            #this draws the green rectangle around the persons face  and loops
            for (x,y,w,h) in faces_rect:
                #crop out images
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done -------------------------')
#converting both to nmupy array
features = np.array(features,dtype='object')
labels = np.array(labels)
# we have 18 faces
#print(f'length of the feauteres  = {len(features)}')
# and 18 corrsponding labels to these faces 
#print(f'length of the lables  = {len(labels)}')


faces_recognizer = cv.face.LBPHFaceRecognizer_create()


#train the rectangle on the feature list and labels list 
faces_recognizer.train(features,labels)


faces_recognizer.save('face_trained.yml')
np.save('feautes.npy',features)
np.save('labels.npy',labels)


