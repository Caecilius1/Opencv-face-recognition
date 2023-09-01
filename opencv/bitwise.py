import cv2 as cv

import numpy as np

blank = np.zeros((400, 400), dtype= 'uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('Circle', circle)

#bitwise and

bit_wise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('and', bit_wise_and)
#
bit_wise_not = cv.bitwise_xor(rectangle,circle)
cv.imshow("not", bit_wise_not)

cv.waitKey(0)