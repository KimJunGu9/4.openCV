import cv2
import sys

src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('영상을 불러올 수 없습니다.')
    sys.exit()

print('src.shape:', src.shape) #(480, 640, 3)
print('src.dtype:', src.dtype) #uint8

b_plane, g_plane, r_plane = cv2.split(src) # b,g,r순서  # 색분할


# split() 사용하지 않고 뽑아보기 (위와 아래는 같은 말임)
# b_plane = src[:,:,0]
# g_plane = src[:,:,1]
# r_plane = src[:,:,2]


cv2.imshow('src', src)
cv2.imshow('b_plane', b_plane)  # 제일 밝은색이 뽑아놓은 그 색깔임 # 파란색을 뽑았으니 파란색부위가 제일 밝음
cv2.imshow('g_plane', g_plane)
cv2.imshow('r_plane', r_plane)
cv2.waitKey()

cv2.destroyAllWindows()