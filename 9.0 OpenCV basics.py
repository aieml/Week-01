import cv2 #library for image processing

img=cv2.imread('Samples/flower.jpg')

#print(img.shape)

#print(img[100][100])

img[100:150,:]=[255,0,0]

cv2.imshow('WINDOW',img)
