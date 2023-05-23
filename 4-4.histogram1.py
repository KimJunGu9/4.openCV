import sys

import cv2
import matplotlib.pyplot as plt

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 읽어올 수 없습니다.')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])

# src : 소스를 집어넣을때 리스트형식으로 집어넣으니까 [src] 로 집어넣음
# 0 : channel
# none : mask
# 256 : hisSize
# 0, 256 : ranges

cv2.imshow('src', src)
cv2.waitKey(1)

plt.plot(hist)
plt.show()