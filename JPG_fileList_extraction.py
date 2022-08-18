import os

file_list = os.listdir()
jpg_file_list=[]
for file in file_list:
    name,ext = os.path.splitext(file)
    if '.jpg' == ext:
        #print('file name',file)
        jpg_file_list.append(file)
f = open('JPG_file_list.txt','w')
for x in jpg_file_list:
    f.write(x)
    f.write('\n')
f.close()
print('Program finished....')
