import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Project\img\image.jpg')
cv.imshow('Flower', img)

# Define a maximum display size
max_display_size = (800, 600)

# Resize the image if it exceeds the maximum display size
height, width = img.shape[:2]
if height > max_display_size[1] or width > max_display_size[0]:
    img = cv.resize(img, max_display_size, interpolation=cv.INTER_AREA)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)