import cv2
import sys

src = cv2.imread('field.bmp')
hero = cv2.imread('hero.png',cv2.IMREAD_UNCHANGED) # png파일을 불러올 때 UNCHANGED를 써야한다.

if src is None or hero is None:
    print('영상을 불러올 수 없습니다.')
    sys.exit()
    


mask = hero[:,:,3] # 3은 컬러채널을 뜻함. b,g,r을 가지고 있음
hero = hero[:,:,:-1] # hero는 b, g, r 3채널, png는 4채널(b, g, r, a) # 알파값은 투명도를 주는 것(채널)임
                     # 그래서 [:,:,:]에서 마지막 :는 4채널을 뜻하는데 a(알파값)을 빼려면 -1을 해야 됨

h, w = mask.shape[:2] # 채널이 3채널이니까 처음부터 2번째가되기전까지, 즉 0, 1 을 뽑으면 h,w을 뽑을 수 있다
crop = src[10:10+h,10:10+w] #위치를 잡아주는거라서 크게 생각안해도 됨

cv2.copyTo(hero, mask ,crop) # hero(전체)에서 mask에 해당하는것만 추출해서 crop위치에 붙인다.

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('hero', hero)
cv2.waitKey()
cv2.destroyAllWindows()