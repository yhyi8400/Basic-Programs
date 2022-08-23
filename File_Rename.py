# File Name Changes

import os
import shutil

file_list_path= "test"

DESTINATION_DIR = "File_Rename"

File_rename = 'plate_'

def start(dir_name):
    if not os.path.exists(DESTINATION_DIR):
        os.makedirs(DESTINATION_DIR)
    count = 1
    for jpg_filename in os.listdir(file_list_path):
        if jpg_filename.endswith('jpg'):
            jpg_index = jpg_filename.index('.')
            jpg_file_name = jpg_filename[:jpg_index]

            for txt_filename in os.listdir(file_list_path):
                if txt_filename.endswith('txt'):
                    txt_index = txt_filename.index('.')
                    txt_file_name = txt_filename[:txt_index]
                    if jpg_file_name == txt_file_name:

                        jpg_file_rename = File_rename+jpg_file_name+'_'+str(count)+'.jpg'
                        txt_file_rename = File_rename+jpg_file_name+'_'+str(count)+'.txt'
                        
                        jpg_og_path = os.path.join(dir_name+'/'+file_list_path, jpg_filename)
                        txt_og_path = os.path.join(dir_name+'/'+file_list_path, txt_filename)

                        jpg_target_path = os.path.join(dir_name+'/'+DESTINATION_DIR, jpg_file_rename)
                        txt_target_path = os.path.join(dir_name+'/'+DESTINATION_DIR, txt_file_rename)
                        shutil.copyfile(jpg_og_path, jpg_target_path)
                        shutil.copyfile(txt_og_path, txt_target_path)
                        
                        print(jpg_target_path,txt_target_path)

                        count += 1
                        
                
                    #read_file(dir_name,filename)
            #print(count,filename, file_name)
        #else:
        #    print("Skipping file: {}".format(filename))

        


if __name__ == "__main__":
    dir_path=(os.getcwd())  #G:\자동차번호판영상
    print(dir_path)
    start(dir_path)
