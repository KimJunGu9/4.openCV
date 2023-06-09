import cv2
import sys

src = cv2.imread('candies.png')

if src is None:
    print('영상을 읽어올 수 없습니다.')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100)) # 하한값 : (0, 128, 0), 상한값 : (100, 255, 100)
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))  # 하한값 : (50, 150, 0), 상한값 : (80, 255, 255)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()