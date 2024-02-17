import cv2 as cv

# Read in an image
img = cv.imread(r'C:\Project\img\image.jpg')

# Define a maximum display size
max_display_size = (800, 600)

# Resize the image if it exceeds the maximum display size
height, width = img.shape[:2]
if height > max_display_size[1] or width > max_display_size[0]:
    img = cv.resize(img, max_display_size, interpolation=cv.INTER_AREA)

cv.imshow('Flower', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
