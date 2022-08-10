import glob
import os

# .txt 파일이 있는 폴더를 지정
file_path = 'test/*.txt'

# 출력 폴더를 지정
file_out = 'out/'

out_path = file_out

original_class = input('원래 있던 클래스 번호:')
modified_class = input('수정 하고자하는 클래스 번호:')

file_list = glob.glob(file_path)
#print(file_list)
for file in file_list:
    f_r = open(file,'r')
    out_file=os.path.basename(file)
    out_path = out_path + out_file
    f_w = open(out_path,'a')
    #print(out_path)
    lines = f_r.readlines()
    for line in lines:
        class_num = line[:1]
        bounding_box_value = line[1:]
        
        if class_num == original_class: class_result = modified_class
        else: class_result = class_num
        
        new_data = class_result + '' + bounding_box_value
        f_w.write(new_data)
        
        print(new_data)
        
        
    f_r.close()
    f_w.close()
    out_path = file_out



