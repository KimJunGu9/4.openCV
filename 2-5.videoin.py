import cv2
import sys

# 동영상 들여오기

cap = cv2.VideoCapture('Lake.mp4') # 캠을 들여오고싶으면 0을 넣고, 동영상을 불러오고싶으면 동영상이름을 넣는다.

if not cap.isOpened():
    print('동영상을 열 수 없습니다.')
    sys.exit()

print('가로 사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('프레임 수 : ', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

# fps = cap.get(cv2.CAP_PROP_FPS)
# print('FPS : ', fps)
print('FPS  : ', int(cap.get(cv2.CAP_PROP_FPS)))


while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()


