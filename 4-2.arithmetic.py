import cv2
import sys

import matplotlib.pyplot as plt

src1 = cv2.imread('lenna2.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('영상을 불러올 수 없습니다.')
    sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U)
dst2 = cv2.subtract(src1, src2)
dst3 = cv2.absdiff(src1, src2)


plt.subplot(221), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
plt.subplot(222), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
# 흰색은 어디를 더하든 흰색이다.
plt.subplot(223), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('subtract')
# 전체에서 흰색을 빼면 검은색이 나온다.
plt.subplot(224), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('absdiff')
plt.show()
