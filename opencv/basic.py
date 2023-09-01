import cv2 as cv



img = cv.imread('Photos/mehmet.jpg')

cv.imshow('Mehmet', img)

#converting to grayscale = Griye çevirme
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#blurlama 
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade = Animated
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating the image = genişletme
dilated = cv.dilate(canny, (3, 3), iterations=5)
cv.imshow('Dilated', dilated)

#eroding = aşındırma
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroding', eroded)

#resize
resize = cv.resize(img, (500,500))
cv.imshow('resized', resize)

#ccrapping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
       