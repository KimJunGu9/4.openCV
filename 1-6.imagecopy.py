import cv2

# img1 = cv2.imread('dog.jpg')
# img2 = img1
# img3 = img1.copy()

img1 = cv2.imread('dog.jpg')
img2 = img1[64:300, 165:450] # openCV에서는 가로와 세로가 바뀌어서 나와있으므로 [h(세로),w(가로)]이다.
img3 = img1[64:300, 165:450].copy()  # 그래서 [세로, 가로] 중 가로는 165부터 450까지, 세로는 64부터 300까지 이다.


img2.fill(0)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()