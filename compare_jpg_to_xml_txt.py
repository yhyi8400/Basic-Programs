# JPG 영상과 XML, TXT파일을 비교하여 결과를 나타냄
# 본 파일을 찾고자 하는 폴더 밖에 두고 원하는 폴더 이름을 지정
# Programed by Z-AI Lab


import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join

dirs = ['5.images_plate'] 

def getImagesInDir(dir_path):
    image_list = []
    for filename in glob.glob(dir_path + '/*.jpg'):
        image_list.append(filename)

    return image_list

def getXmlInDir(dir_path):
    xml_list = []
    for filename in glob.glob(dir_path + '/*.xml'):
        xml_list.append(filename)

    return xml_list

def getTxtInDir(dir_path):
    txt_list = []
    for filename in glob.glob(dir_path + '/*.txt'):
        txt_list.append(filename)

    return txt_list

cwd = getcwd()

for dir_path in dirs:
    full_dir_path = cwd + '/' + dir_path
    jpg_image_paths = getImagesInDir(full_dir_path)
    xml_image_paths = getXmlInDir(full_dir_path)
    txt_image_paths = getTxtInDir(full_dir_path)

    file_list = os.listdir(full_dir_path)

    file_list_jpg = [file for file in file_list if file.endswith(".jpg")]
    file_list_xml = [file for file in file_list if file.endswith(".xml")]
    file_list_txt = [file for file in file_list if file.endswith(".txt")]

    name_list_jpg=[]
    name_list_xml=[]
    name_list_txt=[]
    
    for jpg_name in file_list_jpg:
        name_list_jpg.append(os.path.splitext(jpg_name)[0])
    for xml_name in file_list_xml:
        name_list_xml.append(os.path.splitext(xml_name)[0])
    for txt_name in file_list_txt:
        name_list_txt.append(os.path.splitext(txt_name)[0])

    jpg_xml = list(set(name_list_jpg)-set(name_list_xml))
    jpg_txt = list(set(name_list_jpg)-set(name_list_txt))

    print("jpg - xml",end='\n')
    print(jpg_xml)
    print("Number:",len(jpg_xml))

    print("jpg - txt",end='\n')
    print(jpg_txt)
    print("Number:",len(jpg_txt))


    print("Finished processing: " + dir_path)
