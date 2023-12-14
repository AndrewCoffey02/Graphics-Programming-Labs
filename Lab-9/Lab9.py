import cv2
import numpy as np
from matplotlib import pyplot as plt
import copy

img = cv2.imread('ATU1.jpg', )

imgHarris = copy.deepcopy(img)

gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.cornerHarris(gray_scale, 2, 3, 0.04)

cv2.imshow('dst', dst)
cv2.waitKey(0)

