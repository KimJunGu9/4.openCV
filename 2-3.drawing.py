import cv2
import numpy as np

img = np.full((400,400,3), 255, np.uint8) # 400,400짜리 컬러채널(3)인데 255(흰색)으로 채움


cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
# pt1 : (50,50)
# pt2 : (200,50)
# color : (0,0,255)(b,g,r)
# thickness : 5



cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
# rec : (50, 200, 150, 100)
# color : (0, 255, 0)
# thickness : 2

cv2.rectangle(img, (70, 220, 150, 100), (0, 120, 0), -1)
# rec : (70, 220, 150, 100)
# color : (0, 120, 0)
# thickness : -1



cv2.circle(img, (300, 100), 50, (255, 255, 0), -1)
# center : (300, 100)
# radius : 50
# color : (255,255,0)
# thickness : -1



text = 'Hello, Python'
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
# org : (50, 350)
# fontFace : cv2.FONT_HERSHEY_SIMPLEX
# fontScale : 0.8,
# color : (0, 0, 255)


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()