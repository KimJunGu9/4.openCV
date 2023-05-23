import cv2
import sys

# 캠 들여오기

cap = cv2.VideoCapture('Lake.mp4') # VideoCapture이 하는 기능을 Cap이 전부 기능을 부여받음

if not cap.isOpened():
    print('동영상을 열 수 없습니다')
    sys.exit()

print('가로 사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('프레임 수 : ', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv2.CAP_PROP_FPS)
print('FPS : ', fps)
# print('FPS  : ', int(cap.get(cv2.CAP_PROP_FPS)))  # 위와 같음

while True:
    ret, frame = cap.read()  # ret은 True or False가 온다.   / frame에는 이미지가 들어감

    if not ret:        # 읽어들어온게 없으면 반복문을 끝냄
        break

    # inversed = ~frame # ~ (물결모양)은 반전된 화면을 보여주기 위한

    cv2.imshow('frame', frame)
    # cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27:  # 1000이 1초이므로 10은 0.001초  // 27은 esc키
        break

cap.release()  # 캠을 끄고
cv2.destroyAllWindows() # 창을 닫음



