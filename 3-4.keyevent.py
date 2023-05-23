import cv2

# 키 이벤트

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)

while True:
    keyvalue = cv2.waitKey()  # 키 이벤트
    if keyvalue == ord('i') or keyvalue == ord('I'): # i 또는 I를 누르면  # ord()는 아스키코드 뽑는 함수
        img = ~img   # 이미지를 반전시켜서 보여준다.
        cv2.imshow('image', img)
    elif keyvalue == 27:  # esc(27)을 누르면 나가짐
        break

cv2.destroyAllWindows()