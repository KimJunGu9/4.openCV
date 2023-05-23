import cv2
import sys
import numpy as np

src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 불러올 수 없습니다.')
    sys.exit()

gmin, gmax, _, _ = cv2.minMaxLoc(src)  
# _ : minMaxLoc에서 리턴받는 값(아직 정해지지않음), 리턴값을 받아서 버리겠다는 의미

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
#dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8)  # 위와 아래(수식)는 같다
# dst = None
# 0 = alpha
# 255 = beta



cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()