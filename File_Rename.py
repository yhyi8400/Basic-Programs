# File Name Changes
# 원본 영상 폴더 지정: 'file_list_path'
# 파일 이름 변경 후 저장할 폴더 지정:  'DESTINATION_DIR'


import os
import shutil

file_list_path= "images_plate"

DESTINATION_DIR = "File_Rename_Result"

File_rename = 'plate_'

def start(dir_name):
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)
    count = 1
    
    
    for jpg_filename in os.listdir(file_list_path):
        if jpg_filename.endswith('jpg'):
            jpg_index = jpg_filename.index('.')
            jpg_file_name = jpg_filename[:jpg_index]

            txt_status = True
            xml_status = False

            for filename in os.listdir(file_list_path):
                if filename.endswith('txt'):
                    txt_index = filename.index('.')
                    txt_file_name = filename[:txt_index]
                    if jpg_file_name == txt_file_name:

                        jpg_file_rename = File_rename+jpg_file_name+'_'+str(count)+'.jpg'
                        txt_file_rename = File_rename+jpg_file_name+'_'+str(count)+'.txt'
                        
                        jpg_og_path = os.path.join(dir_name+'/'+file_list_path, jpg_filename)
                        txt_og_path = os.path.join(dir_name+'/'+file_list_path, filename)

                        jpg_target_path = os.path.join(dir_name+'/'+DESTINATION_DIR, jpg_file_rename)
                        txt_target_path = os.path.join(dir_name+'/'+DESTINATION_DIR, txt_file_rename)
                        shutil.copyfile(jpg_og_path, jpg_target_path)
                        shutil.copyfile(txt_og_path, txt_target_path)
                        
                        txt_status = True
                        
                elif filename.endswith('xml'):
                    xml_index = filename.index('.')
                    xml_file_name = filename[:xml_index]
                    if jpg_file_name == xml_file_name:

                        jpg_file_rename = File_rename+jpg_file_name+'_'+str(count)+'.jpg'
                        xml_file_rename = File_rename+jpg_file_name+'_'+str(count)+'.xml'
                        
                        jpg_og_path = os.path.join(dir_name+'/'+file_list_path, jpg_filename)
                        xml_og_path = os.path.join(dir_name+'/'+file_list_path, filename)

                        jpg_target_path = os.path.join(dir_name+'/'+DESTINATION_DIR, jpg_file_rename)
                        xml_target_path = os.path.join(dir_name+'/'+DESTINATION_DIR, xml_file_rename)
                        shutil.copyfile(jpg_og_path, jpg_target_path)
                        shutil.copyfile(xml_og_path, xml_target_path)

                        xml_status = True
                        
                        #print(jpg_target_path,txt_target_path,xml_target_path)

            if xml_status == True and txt_status == True:
                count += 1
            
            elif xml_status == True and txt_status == False:
                count += 1
            
            elif xml_status == False and txt_status == True:
                count += 1

            print('Count:',count-1)
                        
                
                    #read_file(dir_name,filename)
                #print(count)


        


if __name__ == "__main__":
    dir_path=(os.getcwd())  #G:\자동차번호판영상
    print(dir_path)
    start(dir_path)
    print('Processing Finished!!')
