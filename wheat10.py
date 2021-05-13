#coding=utf-8
import arcpy
from arcpy.sa import *
from arcpy import env
import os

savepath=r"I:/SMID_product(wheat10)" #输入文件路径
for x in range(2,3):
    for y in range(1993 + (x-1)*2 , 1995 + (x-1)*2):  # 处理年份，需要修改
        outpath = savepath + "/" + str(y)
        arcpy.env.workspace = outpath
        list = os.listdir(outpath)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
            name = str(list[i])
            name2 = name[0:7]
            shp = r"C:/Users/win/Desktop/cn_country/wheat10/wheat83 - 副本 (" + str(x) + ").shp"
            ExtractMultiValuesToPoints(shp, [[name, name2],
                                             ], "NONE")
