import cv2
import sys
import numpy as np

src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 불러올 수 없습니다.')
    sys.exit()

# kernel = np.ones((3,3), dtype=np.float64) /9.
# dst = cv2.filter2D(src, -1, kernel)

dst = cv2.blur(src, (3,3))  # 위에 두 줄이랑 같음  ksize : 3,3


cv2.imshow('src', src) # 날카로워짐
cv2.imshow('dst', dst) # 부드러워짐
cv2.waitKey()

cv2.destroyAllWindows()