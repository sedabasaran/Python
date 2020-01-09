import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
kamera.set(3, 640)  # set width en
kamera.set(4, 480)  # set hight

# define range of .. color in HSV (blue) -mavi renk
dusuk = np.array([85, 50, 50])
yuksek = np.array([135, 255, 255])

while True:  

    ret, goruntu = kamera.read()  # ret kamarenın açık olup olmadığını kontrol ediyor açıksa True.
    hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, dusuk, yuksek)  # hsv göre dusuk ,yuks filtreleme yaptık.

    # Bitwise-AND mask and original image
    sonResim = cv2.bitwise_and(goruntu, goruntu, mask=mask)

    cv2.imshow('BGR ANA GORUNTU', goruntu)

    cv2.imshow("mask", mask)

    cv2.imshow("renk algılama", sonResim)

    cv2.imshow('HSV',hsv)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()
