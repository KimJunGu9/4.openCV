import cv2
import numpy as np

oldx = oldy = -1  # 함수 바깥에 있으니 전역변수

# 마우스 이벤트

def on_mouse(event, x, y, flags, param):
    global oldx, oldy  # global : 밖에 있는 전역변수를 사용할 수 있게 설정

    if event == cv2.EVENT_LBUTTONDOWN:  # 마우스 왼쪽버튼이 눌렸다면
        oldx, oldy = x, y
        print('왼쪽 버튼 클릭: %d, %d' % (x, y))
    elif event == cv2.EVENT_LBUTTONUP:  # 마우스 왼쪽 버튼을 땠다면
        print('왼쪽 버튼 땜: %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 커서가 움직였다면
        if flags & cv2.EVENT_FLAG_LBUTTON: # 마우스 이벤트가 벌어지고 있는 상황에서 L버튼이 눌러져있는 상태라면
            cv2.line(img, (oldx, oldy), (x, y), (255, 51, 255), 3, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y


img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
