import cv2
import sys

src = cv2.imread('airplane.bmp')
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp')

if src is None or mask is None or dst is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()


# src, mask, dst는 모두 크기가 같아야 함
# src와 dst는 같은 타입이어야 하며, mask는 반드시 그레이스케일 타입의 이진 영상이어야 한다!!!
cv2.copyTo(src, mask, dst)  # src(원본)에 있던 것을 mask(관심영역)를 골라서 dst(결과값)에 붙여준다.

# dst는 원래 비행기가 없고 잔디밭만 있음

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()





