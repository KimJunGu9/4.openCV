import cv2
import sys

cap1 = cv2.VideoCapture('Lake.mp4')
cap2 = cv2.VideoCapture('puma.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('비디오를 열 수 없습니다')
    sys.exit()

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))  # 영상을 읽어와서 프레임 갯수를 frame_cnt1에 저장함
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)

print('frame_cnt1: ', frame_cnt1)
print('frame_cnt2: ', frame_cnt2)
print('fps: ', fps)

delay = int(1000 / fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # DIVX로 저장

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))  # 출력영상은 output.avi로 저장

# while로 써도 무방함. 다른방식임.

for i in range(frame_cnt1):
    ret1, frame1 = cap1.read()

    out.write(frame1)
    cv2.imshow('output', frame1)
    cv2.waitKey(delay)

for i in range(frame_cnt2):
    ret2, frame2 = cap2.read()

    out.write(frame2)
    cv2.imshow('output', frame2)
    cv2.waitKey(delay)

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()

# Lake.mp4를 읽어 output.avi로 저장.
