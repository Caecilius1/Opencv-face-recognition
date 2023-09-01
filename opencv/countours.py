import cv2 as cv

img = cv.imread('Photos/mehmet.jpg')

cv.imshow('Mehmet', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

'''blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125,175)
cv.imshow('Canny Edges', canny)'''

ret, thresh = cv.treshold(gray, 125, 255, cv.THRESH_BINARY)



contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found !')



cv.waitKey(0)