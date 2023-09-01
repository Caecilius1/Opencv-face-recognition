import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#1.paint the image

blank[200:300, 300:400] = 0,255,0
cv.imshow('Green',blank)

#2.rectangle
''' (blank.shape[1]//2, blank.shape[0]//2)#bu köşe dikdörtgeni# '''
cv.rectangle(blank, (0,0), (250, 480), (0,255,0), thickness=2) #thickness=cv.FILLED && -1 dersen dikdörtgen dolar
cv.imshow('Rectangle', blank)


#Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
cv.imshow('Circle', blank)

#line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)

#text
cv.putText(blank, 'Hello', (250, 380), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)