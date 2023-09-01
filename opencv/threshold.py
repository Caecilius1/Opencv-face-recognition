import cv2 as cv

img = cv.imread('Photos/mehmet.jpg')
cv.imshow('image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#thresholding
threshold, thresh = cv.threshold(img, 100, 155, cv.THRESH_BINARY)
cv.imshow('thresholded', thresh)

threshold, thresh_inv = cv.threshold(img, 150, 155, cv.THRESH_BINARY_INV)
cv.imshow('thresholded inv', thresh_inv)

#adaptive
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 3)
cv.imshow('adaptive_thresh', adaptive_thresh)


cv.waitKey(0)
