import cv2
import sys

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

dst = cv2.add(src, 100) # 기존(src)의 밝기를 100만큼 올려서 dst에 저장



src2 = cv2.imread('lenna.bmp')

if src2 is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

dst2 = cv2.add(src2, (100, 100, 100, 0))
# 영상값 뒤에 스칼라값이 하나의 자연수일 수도 있고 튜플일 수도 있다.
# 근데 컬러값은 채널이 3개짜리이기때문에 튜플 안에 3개의 숫자를 쓰는데, 뒤에 상수가 들어가면 안되기때문에 0을 집어넣는다.


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('src2', src2)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()
