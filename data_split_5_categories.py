import os
import random
import shutil

## 저장할 폴더 지정
save_split_data_path = 'd:/yolov5/datasets/integrated_system/'
save_fold_list = ['test','train','valid']

### Dataset 읽기(파일이름만)
imgList = ['boar','fire','human','smoke','vehicle']
current_path = os.getcwd()
print(current_path)
for x in imgList:
    data_path = current_path + '/'+ 'total_images'+'/'+ x
    if x == 'boar':
        boar_imgList = os.listdir(data_path)
    elif x == 'fire':
        fire_imgList = os.listdir(data_path)
    elif x == 'human':
        human_imgList = os.listdir(data_path)
    elif x == 'smoke':
        smoke_imgList = os.listdir(data_path)
    elif x == 'vehicle':
        vehicle_imgList = os.listdir(data_path)

    
boar_txt_fileList = []
fire_txt_fileList = []
human_txt_fileList = []
smoke_txt_fileList = []
vehicle_txt_fileList = []

for x in boar_imgList:
    sp = os.path.splitext(x)
    if sp[1] == '.txt':
        boar_txt_fileList.append(sp[0]) 
        
for x in fire_imgList:
    sp = os.path.splitext(x)
    if sp[1] == '.txt':
        fire_txt_fileList.append(sp[0])     

for x in human_imgList:
    sp = os.path.splitext(x)
    if sp[1] == '.txt':
        human_txt_fileList.append(sp[0]) 

for x in smoke_imgList:
    sp = os.path.splitext(x)
    if sp[1] == '.txt':
        smoke_txt_fileList.append(sp[0])

for x in vehicle_imgList:
    sp = os.path.splitext(x)
    if sp[1] == '.txt':
        vehicle_txt_fileList.append(sp[0])
        

#shuffling images
random.shuffle(boar_txt_fileList)
random.shuffle(fire_txt_fileList)
random.shuffle(human_txt_fileList)
random.shuffle(smoke_txt_fileList)
random.shuffle(vehicle_txt_fileList)

#print(boar_txt_fileList[10])
#print(fire_txt_fileList[10])
#print(human_txt_fileList[10])
#print(smoke_txt_fileList[10])
#print(vehicle_txt_fileList[10])


split = 0.2

train_path = save_split_data_path+'train/'
val_path = save_split_data_path+'valid/'

#print(train_path)
#print(val_path)


if os.path.isdir(train_path) == False:
    os.makedirs(train_path)
if os.path.isdir(val_path) == False:
    os.makedirs(val_path)

boar_imgLen = len(boar_txt_fileList)
fire_imgLen = len(fire_txt_fileList)
human_imgLen = len(human_txt_fileList)
smoke_imgLen = len(smoke_txt_fileList)
vehicle_imgLen = len(vehicle_txt_fileList)

#print("Boar Images in total: ", boar_imgLen)
#print("Fire Images in total: ", fire_imgLen)
#print("Human Images in total: ", human_imgLen)
#print("Smoke Images in total: ", smoke_imgLen)
#print("Vehicle Images in total: ", vehicle_imgLen)


boar_train_images = boar_txt_fileList[: int(boar_imgLen - (boar_imgLen*split))]
fire_train_images = fire_txt_fileList[: int(fire_imgLen - (fire_imgLen*split))]
human_train_images = human_txt_fileList[: int(human_imgLen - (human_imgLen*split))]
smoke_train_images = smoke_txt_fileList[: int(smoke_imgLen - (smoke_imgLen*split))]
vehicle_train_images = vehicle_txt_fileList[: int(vehicle_imgLen - (vehicle_imgLen*split))]

boar_val_images = boar_txt_fileList[int(boar_imgLen- (boar_imgLen*split)):]
fire_val_images = fire_txt_fileList[int(fire_imgLen- (fire_imgLen*split)):]
human_val_images = human_txt_fileList[int(human_imgLen- (human_imgLen*split)):]
smoke_val_images = smoke_txt_fileList[int(smoke_imgLen- (smoke_imgLen*split)):]
vehicle_val_images = vehicle_txt_fileList[int(vehicle_imgLen- (vehicle_imgLen*split)):]

print("boar_Training images: ", len(boar_train_images))
print("boar_Validation images: ", len(boar_val_images))
print("fire_Training images: ", len(fire_train_images))
print("fire_Validation images: ", len(fire_val_images))
print("human_Training images: ", len(human_train_images))
print("human_Validation images: ", len(human_val_images))
print("smoke_Training images: ", len(smoke_train_images))
print("smoke_Validation images: ", len(smoke_val_images))
print("vehicle_Training images: ", len(vehicle_train_images))
print("vehicle_Validation images: ", len(vehicle_val_images))


for x in imgList:
    data_path = current_path + '/'+ 'total_images'+'/'+ x
    if x == 'boar':
        for imgName in boar_train_images:
            boar_img_train_path = train_path + 'images/'
            og_path = os.path.join(data_path, imgName)+'.jpg'
            target_path = os.path.join(boar_img_train_path, imgName)+'.jpg'
            shutil.copyfile(og_path, target_path)

            boar_lab_train_path = train_path + 'labels/'
            og_txt_path = os.path.join(data_path, imgName)+'.txt'
            target_txt_path = os.path.join(boar_lab_train_path, imgName)+'.txt'
            shutil.copyfile(og_txt_path, target_txt_path)

    elif x == 'fire':
        for imgName in fire_train_images:
            fire_img_train_path = train_path + 'images/'
            og_path = os.path.join(data_path, imgName)+'.jpg'
            target_path = os.path.join(fire_img_train_path, imgName)+'.jpg'
            shutil.copyfile(og_path, target_path)
            
            fire_lab_train_path = train_path + 'labels/'
            og_txt_path = os.path.join(data_path, imgName)+'.txt'
            target_txt_path = os.path.join(fire_lab_train_path, imgName)+'.txt'
            shutil.copyfile(og_txt_path, target_txt_path)
            
    elif x == 'human':
        for imgName in human_train_images:
            human_img_train_path = train_path + 'images/'
            og_path = os.path.join(data_path, imgName)+'.jpg'
            target_path = os.path.join(human_img_train_path, imgName)+'.jpg'
            shutil.copyfile(og_path, target_path)
            
            human_lab_train_path = train_path + 'labels/'
            og_txt_path = os.path.join(data_path, imgName)+'.txt'
            target_txt_path = os.path.join(human_lab_train_path, imgName)+'.txt'
            shutil.copyfile(og_txt_path, target_txt_path)
            
    elif x == 'smoke':
        for imgName in smoke_train_images:
            smoke_img_train_path = train_path + 'images/'
            og_path = os.path.join(data_path, imgName)+'.jpg'
            target_path = os.path.join(smoke_img_train_path, imgName)+'.jpg'
            shutil.copyfile(og_path, target_path)
            
            smoke_lab_train_path = train_path + 'labels/'
            og_txt_path = os.path.join(data_path, imgName)+'.txt'
            target_txt_path = os.path.join(smoke_lab_train_path, imgName)+'.txt'
            shutil.copyfile(og_txt_path, target_txt_path)
            
    elif x == 'vehicle':
        for imgName in vehicle_train_images:
            vehicle_img_train_path = train_path + 'images/'
            og_path = os.path.join(data_path, imgName)+'.jpg'
            target_path = os.path.join(vehicle_img_train_path, imgName)+'.jpg'
            shutil.copyfile(og_path, target_path)
            
            vehicle_lab_train_path = train_path + 'labels/'
            og_txt_path = os.path.join(data_path, imgName)+'.txt'
            target_txt_path = os.path.join(vehicle_lab_train_path, imgName)+'.txt'
            shutil.copyfile(og_txt_path, target_txt_path)


for x in imgList:
    data_path = current_path + '/'+ 'total_images'+'/'+ x
    if x == 'boar':
        for imgName in boar_val_images:
            boar_img_val_path = val_path + 'images/'
            og_path = os.path.join(data_path, imgName)+'.jpg'
            target_path = os.path.join(boar_img_val_path, imgName)+'.jpg'
            shutil.copyfile(og_path, target_path)
            
            boar_lab_val_path = val_path + 'labels/'            
            og_txt_path = os.path.join(data_path, imgName)+'.txt'
            target_txt_path = os.path.join(boar_lab_val_path, imgName)+'.txt'
            shutil.copyfile(og_txt_path, target_txt_path)

    elif x == 'fire':
        for imgName in fire_val_images:
            fire_img_val_path = val_path + 'images/'
            og_path = os.path.join(data_path, imgName)+'.jpg'
            target_path = os.path.join(fire_img_val_path, imgName)+'.jpg'
            shutil.copyfile(og_path, target_path)

            fire_lab_val_path = val_path + 'labels/'             
            og_txt_path = os.path.join(data_path, imgName)+'.txt'
            target_txt_path = os.path.join(fire_lab_val_path, imgName)+'.txt'
            shutil.copyfile(og_txt_path, target_txt_path)
            
    elif x == 'human':
        for imgName in human_val_images:
            human_img_val_path = val_path + 'images/'
            og_path = os.path.join(data_path, imgName)+'.jpg'
            target_path = os.path.join(human_img_val_path, imgName)+'.jpg'
            shutil.copyfile(og_path, target_path)

            human_lab_val_path = val_path + 'labels/'             
            og_txt_path = os.path.join(data_path, imgName)+'.txt'
            target_txt_path = os.path.join(human_lab_val_path, imgName)+'.txt'
            shutil.copyfile(og_txt_path, target_txt_path)

    elif x == 'smoke':
        for imgName in smoke_val_images:
            smoke_img_val_path = val_path + 'images/'
            og_path = os.path.join(data_path, imgName)+'.jpg'
            target_path = os.path.join(smoke_img_val_path, imgName)+'.jpg'
            shutil.copyfile(og_path, target_path)

            smoke_lab_val_path = val_path + 'labels/'             
            og_txt_path = os.path.join(data_path, imgName)+'.txt'
            target_txt_path = os.path.join(smoke_lab_val_path, imgName)+'.txt'
            shutil.copyfile(og_txt_path, target_txt_path)

    elif x == 'vehicle':
        for imgName in vehicle_val_images:
            vehicle_img_val_path = val_path + 'images/'
            og_path = os.path.join(data_path, imgName)+'.jpg'
            target_path = os.path.join(vehicle_img_val_path, imgName)+'.jpg'
            shutil.copyfile(og_path, target_path)

            vehicle_lab_val_path = val_path + 'labels/'             
            og_txt_path = os.path.join(data_path, imgName)+'.txt'
            target_txt_path = os.path.join(vehicle_lab_val_path, imgName)+'.txt'
            shutil.copyfile(og_txt_path, target_txt_path)


print("Done! ")

