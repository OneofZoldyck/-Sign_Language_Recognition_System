import numpy as npy
import cv2
import os
import csv
from imageProcessing import func

if not os.path.exists("data2"):
    os.mkdirs("data2")
if not os.path.exists("data2/train"):
    os.mkdirs("data2/train")
if not os.path.exists("data2/test"):
    os.mkdirs("data2/train")

path1 = "train"
path2 = "data2"
a = ['label']

for i in range(64*64):
    a.append("pixel"+str(i))

label, var, c1, c2 = 0

for(dirpath, dirnames, filenames) in os.walk(path1):
    for dirname in dirnames:
        print(dirname)
        for(direcpath, direcnames, files) in os.walk(path1+"/"+dirname):
            if not os.path.exists(path2+"/train"+dirname):
                os.makedirs(path2+"/train"+dirname)
            if not os.path.exists(path2+"/test"+dirname):
                os.makedirs(path2+"/test"+dirname)
            
            num = 100000000000000000
            i = 0
            for file in files:
                var+=1
                actual_path1 = path1+"/"+dirname+"/"+file
                actual_path2 = path2+"/"+"train/"+dirname+"/"+file
                actual_path3 = path2+"/"+"test/"+dirname+"/"+file
                img = cv2.imread(actual_path1, 0)
                bw_image = func(actual_path1)
                if i < num:
                    c1 += 1
                else:
                    c2 += 1
                    cv2.imwrite(actual_path3, bw_image)
                
                i = i+1
            
            label = label+1
print(var+'\n'+c1+'\n'+c2)

                                                     