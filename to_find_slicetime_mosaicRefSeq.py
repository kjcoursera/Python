# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 20:30:37 2018

@author: kanchana
"""


import pydicom
import re
import glob
import os

mylist = [f for f in glob.glob("Y:\Documents\Teri\Studyfolders\BAC\ASL2D_Notes\VSMK_dicoms\V*_REST")]

params=[]

for file in mylist:
    head,tail = os.path.split(file)
    ds = pydicom.dcmread(file)
    for line in ds:
        if re.match("(.*)(M|m)osaic(.*)", str(line)):
            if re.match("(.*)FD(.*)", str(line)):
#                case = {'seriesname': ds.SeriesDescription, 'slicetime': line[:-10][1] }
                case =  {'slicetime': line[:-10][1] }
                params.append(case)
                
                #params[tail].append("SeriesName:" : ds.SeriesDescription, "slicetime":line[:-10])

for d in params:
    for k,v in d.items():
        print(v)
        
for i in mylist:
    print(i)