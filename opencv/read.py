import cv2 as cv
## image capture
'''img = cv.imread('Photos/mehmet2.jpg')

cv.imshow('Mehmet', img)

cv.waitKey(0)
'''
##Video Capture
capture = cv.VideoCapture('Videos/Video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows() 

