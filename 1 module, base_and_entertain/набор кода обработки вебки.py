import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
res, img=cap.read()
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
color_low1= (0, 100, 100)
color_high1= (15, 255, 255)

color_low2= (165, 100, 100)
color_high2= (180, 255, 255)

img_thresh1=cv2.inRange(img_hsv, color_low1, color_high1)
img_thresh2=cv2.inRange(img_hsv, color_low2, color_high2)
img_thresh=cv2.bitwise_or(img_thresh1, img_thresh2)

cv2.imshow('img_thresh', img_thresh)
moments=cv2.moments(img_thresh)
# Вполне возможно, что ничего в наш диапазон не попало.
# В этом случае момент `m00` будет равен нулю, и делить
# на него нельзя. Учтём это в наших расчётах.
if moments["m00"] !=0.0:
# Для рисования круга вокруг центра масс нам нужны
# целочисленные координаты, поэтому результат деления
# приводим к целым:
cnt_x=int(moments["m10"] /moments["m00"])
cnt_y=int(moments["m01"] /moments["m00"])
# Рисуем окружность на исходном изображении. Параметры:
# img - исходное изображение,
# (cnt_x, cnt_y) - координаты центра окружности,
# 10 - радиус окружности,
# (0, 255, 0) - цвет круга (B=0, G=255, R=0 - зелёный)
# 3 - толщина линии окружности
img=cv2.circle(img, (cnt_x, cnt_y), 10, (0, 255, 0), 3)
cv2.imshow('image', img)

if cv2.waitKey(13) >0:
break

_____
face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()

    # img = cv2.imread("IMG_20191012_145410_3.jpg")

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        img_gray_face = img_gray[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(img_gray_face, 1.1, 19)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 0, 0), 2)

    cv2.imshow('rez', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()


