import cv2
import numpy as np

picture = cv2.imread("pic.jpg")

if picture is None:
    print('shit, I am lost')

gray_picture = cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)

binary_picture = cv2.threshold(gray_picture,130,255,cv2.THRESH_BINARY)[1]
#binary_picture = cv2.threshold(gray_picture, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

cv2.imshow('Original',picture)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Binary_picture', binary_picture)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Binary_picture.jpg', binary_picture)

edges = cv2.Canny(gray_picture,50,150)
cv2.imshow('Edged', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

small = cv2.resize(picture, None, fx=0.4, fy=0.4)
cv2.imshow('Small', small)
cv2.waitKey(0)
cv2.destroyAllWindows()

ker = np.ones((4,4),np.uint8)
erosion = cv2. erode(picture, ker, iterations=1)
dilation = cv2.dilate(picture, ker, iterations=1)
cv2.imshow('Eroded', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('dilated', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()

median_picture = cv2.medianBlur(picture,7)
cv2.imshow('medianBlur', median_picture)
cv2.waitKey(0)
cv2.destroyAllWindows()