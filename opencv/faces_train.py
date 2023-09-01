import os 
import cv2 as cv
import numpy as np

people = ['Alex de Souza','Andrew Garfield', 'Aragorn', 'Ben Affleck', 'Mehmet']
DIR = r'C:\Users\Caecilius\Desktop\opencv\Faces'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for(x, y, w, h)in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()
print("Training done-----------------")


features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer = cv.face.LBPHFaceRecognizer.create()

#train the recognizer on the features list and label list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')

np.save('Features.npy', features)
np.save('labels.npy',labels)
    