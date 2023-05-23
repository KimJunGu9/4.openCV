import cv2
import numpy as np

# (240, 320) : (h,w) -> 크기

img1 = np.empty((240, 320), dtype=np.uint8) 
img2 = np.zeros((240,320,3), dtype=np.uint8)                 # 0(zeros)으로 채우지만 컬러채널(h,w,3)임 -> 고로 까맣게 보임
img3 = np.ones((240,320), dtype=np.uint8) * 188              # 흑백이니까 곱하면 밝기가 밝아짐
img4 = np.full((240,320,3), (123,777,231), dtype=np.uint8)   # (123,777,231)로 채워서 만들어라

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)

cv2.waitKey()
cv2.destroyAllWindows()