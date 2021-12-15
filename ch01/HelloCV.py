'''
05. 영상 파일 불러와서 출력하기
아래 코드는 이미지/영상 파일을 불러오는 기본 템플릿이다.
'''

import cv2
print('Hello, OpenCV', cv2.__version__)

# bmp 파일 불러오기
img = cv2.imread('./ch01/cat.bmp')

# 파일이 제대로 안 불러져 왔을 경우 예외처리
import sys
if img is None:
    print('Image load failed!')
    sys.exit()
    
# 파일이 제대로 불러와졌다면 창을 생성한다.
cv2.namedWindow('image')              # figure 창 이름 설정
cv2.imshow(winname='image', mat=img)  # winname: 창 이름, mat: 띄울 이미지/영상

# 아무 키를 누르면 화면에 띄워둔 이미지 창을 닫는다.
cv2.waitKey()            # 키보드 입력을 기다리는 함수
cv2.destroyAllWindows()  # 모든 창 닫기