import cv2 as cv

#img = cv.imread('Photos/mehmet2.jpg')
#cv.imshow('Mehmet', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
 
 

#reading videos
capture = cv.VideoCapture('Videos/Video.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, scale=.4)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows() 