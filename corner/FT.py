import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('test3.jpg', 0)
rows, cols = img.shape
mask = np.ones(img.shape, np.uint8)
mask[rows/2-30:rows/2+30, cols/2-30:cols/2+30] = 0

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
fshift = fshift * mask
f2shift = np.fft.ifftshift(fshift)
img_new = np.fft.ifft2(f2shift)
img_new = np.abs(img_new)

# img_new = (img_new - np.amin(img_new)) / (np.amax(img_new) - np.amin(img_new))
plt.subplot(121), plt.imshow(img, 'gray'), plt.title('original')
plt.subplot(122), plt.imshow(img_new, 'gray'), plt.title('Highpass')
plt.show()
