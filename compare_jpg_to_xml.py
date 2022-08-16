import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join

dirs = ['images'] 

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


cwd = getcwd()

for dir_path in dirs:
    full_dir_path = cwd + '/' + dir_path
    jpg_image_paths = getImagesInDir(full_dir_path)
    xml_image_paths = getXmlInDir(full_dir_path)

    file_list = os.listdir(full_dir_path)

    file_list_jpg = [file for file in file_list if file.endswith(".jpg")]
    file_list_xml = [file for file in file_list if file.endswith(".xml")]

    name_list_jpg=[]
    name_list_xml=[]
    for jpg_name in file_list_jpg:
        name_list_jpg.append(os.path.splitext(jpg_name)[0])
    for xml_name in file_list_xml:
        name_list_xml.append(os.path.splitext(xml_name)[0])

    jpg_xml = list(set(name_list_jpg)-set(name_list_xml))

    print("jpg - xml",end='\n')
    print(jpg_xml)
    print("Number:",len(jpg_xml))

    print("Finished processing: " + dir_path)
