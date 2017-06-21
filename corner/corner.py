import cv2
import numpy as np
import sys

img = cv2.imread('test2.jpg')
print img.shape
kernel = np.ones((5, 5), np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
erode = cv2.erode(gray, kernel, iterations=1)
dilate = cv2.dilate(gray, kernel, iterations=2)
morpholo = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
laplation = cv2.Laplacian(img, -1)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
canndy = cv2.Canny(img, 200, 300)
log = cv2.logPolar(img, (512, 376), 100, cv2.INTER_AREA)
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray, 5, 3, 0.04)
# img[dst>0.01 * dst.max()] = [0, 0, 255]
while (True):
    cv2.imshow('erode', erode)
    cv2.imshow('dilate', dilate)
    cv2.imshow('original', gray)
    cv2.imshow('morpholo', morpholo)
    cv2.imshow('laplation', laplation)
    cv2.imshow('sebolx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('canndy', canndy)
    cv2.imshow('log', log)
    if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
        break
cv2.destroyAllWindows()
