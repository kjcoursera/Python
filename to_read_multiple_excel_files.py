# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:01:33 2018

@author: kanchana
"""

import glob
import pandas as pd

# list excel files in a workign directory
my_files = [f for f in glob.glob("*.xlsx")]

# to get a score column from all sheets
# assign an empty score variable
score = [];

# for each files
for file in my_files:
    print(file)

# read the file
    df = pd.read_excel(file)

# read the necessary rows and columns.
    data=df.iloc[2:,:]
# rename the column header
    data=data.rename(columns=data.iloc[0]).drop(data.index[0])

#extract the required column
    df2=data.SCORE
# changing the header based on value in df.columns[1]
    df2=df2.rename(df.columns[1],inplace =True)
    score.append(df2)

# to data frame
final_score = pd.DataFrame(score)

