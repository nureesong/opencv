''' 
06. OpenCV 주요 함수 설명
'''

import cv2

# 1. 영상 파일 불러오기: np.ndarray로 리턴
# img = cv2.imread(filename='./ch01/cat.bmp') # (default) flags = cv2.IMREAD_COLOR 
img = cv2.imread(filename='./ch01/cat.bmp', flags=cv2.IMREAD_GRAYSCALE) # grayscale로 이미지 불러오기
# img = cv2.imread(filename='./ch01/cat.bmp', flags=cv2.IMREAD_UNCHANGED) # png 파일의 알파 채널까지 불러온다.

# 파일 확인
import sys
if img is None:
    print('Image load failed!')
    sys.exit()

    
# 2. 영상 파일 저장하기: 저장 여부(bool) 리턴
cv2.imwrite(filename='./ch01/cat_gray.png', img=img)
# params=[cv2.IMWRITE_JPEG_QUALITY, 90] -> JPG 압축률을 90%로 지정

    
# 3. 새 창 띄우기: figure 창 고유 이름 설정
cv2.namedWindow(winname='image') # 영상에 맞게 창 크기가 고정됨
# flags=cv2.WINDOW_NORMAL -> 창 크기 변경하면 그에 맞게 영상도 resize. 영상이 모니터 해상도보다 큰 경우 유용


# 4. 영상 출력하기
cv2.imshow(winname='image', mat=img)  # winname: 창 이름, mat: 띄울 이미지/영상
# 'image'라는 창이 없으면 자동으로 생성하여 영상을 출력해준다. (cv2.WINDOW_AUTOSIZE 옵션으로)
# 따라서 cv2.namedWindow('image')를 생략해도 무방함.


# 5. 키보드 입력 대기 (항상 imshow와 함께 쓰기)
cv2.waitKey() 
# delay=2000 -> 2000ms 동안 키보드 입력을 기다린다. 아무 키도 입력되지 않으면 자동 종료.
# 입력된 키의 ASCII 코드를 리턴. 키가 입력되지 않으면 -1 리턴.
''' 특정 키를 입력했을 때만 창을 종료
while True:
    if cv2.waitKey() == ord('q'):
        break
'''


# 6. 창 닫기: 아래 코드 생략해도 엔터치면 창 닫힘
# cv2.destroyWindow(winname='image') # 지정한 창 하나만 닫는다.
cv2.destroyAllWindows()  # 열려있는 모든 창을 닫는다.
