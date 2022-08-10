#!/usr/bin/env python
# coding: utf-8

# In[1]:


import glob
import os
import pickle
import xml.etree.ElementTree as ET
from os import listdir, getcwd
from os.path import join


dirs = ['yolo']
Pascal_Class_index = {'fire':0,'smoke':1,'human':2,'boar':3, 'vehicle':4, 'plate':5,'person':2}
XML_FILES = []
TXT_DIRECTORY = './txt/'

def Write_TXT(file_name, width, height, result):
    file_name = file_name[:-3]+'txt'
    file_path = os.path.join(TXT_DIRECTORY,file_name)
    f = open(file_path,'w')
    for i, data in enumerate(result):
        data = f'{data}\n'
        data = data.replace(',','').replace('[','').replace(']','')
        f.write(data)
    f.close()
    


def Read_XML(file_path, file_name):
    tree = ET.parse(file_path)
    root = tree.getroot()
    #print(tree, root)
    size = root.find('size')
    
    width = float(size.find('width').text)
    height = float(size.find('height').text)

    result = list()
    for object in root.findall('object'):
        name = object.find('name').text
        class_index = Pascal_Class_index[name]
        bndbox = object.find('bndbox')
        xmin = float(bndbox.find('xmin').text)
        ymin = float(bndbox.find('ymin').text)
        xmax = float(bndbox.find('xmax').text)
        ymax = float(bndbox.find('ymax').text)
        bnd_width = round((xmax-xmin)/width,6)
        bnd_height = round((ymax-ymin)/height,6)
        x_center = round((xmax+xmin)/2/width,6)
        y_center = round((ymax+ymin)/2/height,6)

        result.append([class_index, x_center, y_center, bnd_width, bnd_height])
        print(class_index, x_center, y_center, bnd_width, bnd_height)
    Write_TXT(file_name = file_name, width = width, height = height, result = result)


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating Directory.'+directory)


def main():
    createFolder(TXT_DIRECTORY)
    for files in os.listdir(os.getcwd()):
        if '.xml' in os.path.splitext(files):
            XML_FILES.append(files)
    cwd = getcwd()
    for file in XML_FILES:
        file_path = os.path.join(cwd+'/'+file)
        Read_XML(file_path, file)


if __name__ == '__main__':
    main()
    
print("Finished processing: ")





