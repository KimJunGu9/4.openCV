import sys

import cv2
import matplotlib.pyplot as plt

src = cv2.imread('lenna.bmp')

if src is None:
    print('영상을 읽어올 수 없습니다.')
    sys.exit()

colors = ['b','g','r']
bgr_planes = cv2.split(src) # 채널을 나누는법. # 변수를 3개로 나눠야하는데 리스트로 저장하려고하면 하나로 받으면 된다.


for (p, c) in zip(bgr_planes, colors):        # p는 plane, c는 color
    hist = cv2.calcHist([p],[0],None, [256],[0,256])
    plt.plot(hist, color=c)

cv2.imshow('src',src)
plt.plot(hist)

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()