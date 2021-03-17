import cv2

img = cv2.imread('123.jpg')

scale_percent = 30
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', gray)

edges = cv2.Canny(gray, threshold1=30, threshold2=100)
cv2.imshow('Edge detect ',edges) # show the detected edges

cv2.waitKey(0)

