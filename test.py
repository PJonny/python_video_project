import cv2
import numpy as np


img = np.zeros((200, 300), dtype=np.uint8)
img[50:150, 80:150] = 255

ret, thresh = cv2.threshold(img, 127, 255, 0)
print ret
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imshow("contours", img)
cv2.waitKey()
cv2.destroyAllWindows()