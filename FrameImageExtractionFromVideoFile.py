# -*- coding: utf-8 -*-
__author__ = 'YHSJH.YI'
 
import cv2
import os



# 비디오 파일 이름 넣기
video_file_name = "sleep_people_without_cover"
file_extended = ".mp4"

video_file_path = video_file_name+file_extended

# 영상 저장 폴더 생성 아래에서 검사하여 없으면 자동 생성
# 파일 이름과 같은 폴더이름 생성
dirname = video_file_name


try:
    if not(os.path.isdir(dirname)):
        os.makedirs(os.path.join(dirname))
except OSError as e:
    if e.error != e.EEXIST:
        print("Failed to create directory!!!!")
        raise


# 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
vidcap = cv2.VideoCapture(video_file_path)
 
count = 0
 
while(True):
    # read()는 grab()와 retrieve() 두 함수를 한 함수로 불러옴
    # 두 함수를 동시에 불러오는 이유는 프레임이 존재하지 않을 때
    # grab() 함수를 이용하여 return false 혹은 NULL 값을 넘겨 주기 때문
    ret, image = vidcap.read()
 
    # 캡쳐된 이미지를 저장하는 함수 
    #cv2.imwrite("Smoke_within_Forest/Smoke_within_Forest_frame%d.jpg" % count, image)
    cv2.imwrite(dirname + "/" + dirname + "_%d.jpg" % count, image)
 
    print('Saved frame%d.jpg' % count)
    cv2.imshow('Streaming Image',image)
    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
vidcap.release()
cv2.destroyAllWindows()
