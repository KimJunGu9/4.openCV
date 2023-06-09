import cv2
import sys
import numpy as np


src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

blr = cv2.GaussianBlur(src, (0,0), 2)
dst = np.clip(2.0 * src - blr, 0, 255).astype(np.uint8)
# clip() : 최소값과 최대값 사이의 값들로 변환


cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
