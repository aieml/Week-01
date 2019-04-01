import cv2 #library for image processing

img=cv2.imread('Samples/flower.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(gray.shape)

cv2.imshow('IMG',gray)
