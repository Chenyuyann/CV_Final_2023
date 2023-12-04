import copy
import cv2
import os
import shutil
import numpy as np

def mask_to_yolo(mask_path, yolo_path):
    path = mask_path
    files = os.listdir(path)
    for file in files:
        name = file.split('.')[0]
        file_path = os.path.join(path,name+'.png')
        img = cv2.imread(file_path)
        H,W=img.shape[0:2]

        gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,bin_img = cv2.threshold(gray_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cnt,hit = cv2.findContours(bin_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_TC89_KCOS)

        cnt = list(cnt)
        with open(os.path.join(yolo_path, "{}.txt".format(name)), "w") as f:
            for j in cnt:
                result = []
                pre = j[0]
                for i in j:
                    if abs(i[0][0] - pre[0][0]) > 1 or abs(i[0][1] - pre[0][1]) > 1:# 在这里可以调整间隔点，我设置为1
                        pre = i
                        temp = list(i[0])
                        temp[0] /= W
                        temp[1] /= H
                        result.append(temp)

                if len(result) != 0:
                    f.write("0 ")
                    for line in result:
                        line = str(line)[1:-2].replace(",","")
                        f.write(line+" ")
                    f.write("\n")
            f.close()

mask_path_train = "/project/train/src_repo/yolov8/datasets/masks/train"
yolo_path_train = "/project/train/src_repo/yolov8/datasets/labels/train"
mask_to_yolo(mask_path_train, yolo_path_train)

mask_path_val = "/project/train/src_repo/yolov8/datasets/masks/val"
yolo_path_val = "/project/train/src_repo/yolov8/datasets/labels/val"
mask_to_yolo(mask_path_val, yolo_path_val)
