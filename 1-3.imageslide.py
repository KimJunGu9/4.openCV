import cv2
import sys
import glob  # glob은 이미지나 특정 파일들을 디렉토리를 뒤져서 한꺼번에 불러오거나, 처리할 수 있게 만드는 라이브러리
             # 파일명을 일일이 안쓰고 한꺼번에 불러올 수 있음

imgs = glob.glob('images\\*.jpg') # images에 있는 모든 jpg를 가져와서 imgs에 저장하면 리스트로 저장됨


if not imgs:
    print('영상을 불러올 수 없습니다.')
    sys.exit()



idx = 0  # 슬라이드 번호를 인덱스라고 하고 0을 시작점으로 둔다.

while True:
    img = cv2.imread(imgs[idx])

    if img is None:
        print('영상을 불러올 수 없습니다')
        break

    cv2.imshow('image', img) # 'image'라는 창 이름,  img를 넣어서 보여줌

    if cv2.waitKey(1000) >= 0: # 1초를 기다렸다가 키값이 안들어오면 넘어가서
        break

    idx += 1               # 1을 더해서

    if idx >= len(imgs):
        idx = 0       # 인덱스가 5보다 커졌을땐 첫 화면으로 넘어가라

cv2.destroyAllWindows()
