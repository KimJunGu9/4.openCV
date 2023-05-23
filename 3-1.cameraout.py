import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라를 열 수 없습니다')
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) # 초당 프레임 수

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 어떤 비디오포멧으로 저장할 지에 대한 객체를 만듦
delay = round(1000 / fps)

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h)) # frameSize : (w, h)

if not out.isOpened():
    print('파일을 열 수 없습니다')
    cap.release() # 카메라 리소스를 반환함. release를 안하면 카메라가 계속 켜져있다.
    sys.exit()

while True:  # 영상의 프레임을 계속 반복해서 화면에 보여줌
    ret, frame = cap.read()  # ret : true와 false가 저장, frame : 영상이 저장

    if not ret:
        break

    out.write(frame)   # 영상을 저장
    cv2.imshow('frame', frame)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()  # 캠을 끔. 영상을 닫는 이유는 내가 저장할만큼 다 저장하고 마지막에 save를 해줘야 함. 그래서 release하는거다. 안그러면 저장이 안될 수도있다.
cv2.destroyAllWindows()

# 영상을 키고 나서 행동을 한 후에 끌때 output.avi로 저장되는 형식을 말하는 거다.