import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ATU.jpg',)
cv2.waitKey(0)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.waitKey(0)

nrows = 2
ncols = 1

plt.subplot(nrows, ncols,1),plt.imshow(img, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray')
plt.title('Grayscale'), plt.xticks([]), plt.yticks([])
plt.show()



