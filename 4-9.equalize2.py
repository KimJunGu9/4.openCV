import cv2
import sys

src = cv2.imread('field.bmp')

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

ycrcb_planes = []
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
ycrcb_planes = cv2.split(src_ycrcb)

ycrcb_planes = list(ycrcb_planes)

# 밝기 성분에 대해서만 히스토그램 평활화 수행하기위해 ycrcb 사용한다.
ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0]) # 밝기를 선택한 후 히스토그램 평활화한 다음에 다시 집어넣는다

dst_ycrcb = cv2.merge(ycrcb_planes)  # 합쳐준 후
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
