# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from dataCalculator.graph import drawGraph
from dataCalculator.cleaning import dataCleaning



# csv 파일 읽기
raw_date = []
raw_vix = []
raw_total = []

script_dir = os.path.dirname(__file__)
rel_path = "dataStorage/VIXCLS0414.csv"
abs_file_path = os.path.join(script_dir,rel_path)

f = open(abs_file_path, 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    raw_date.append(line[0])
    raw_vix.append(line[1])
f.close()

if raw_date[0] == 'DATE':
    del raw_date[0]
if raw_vix[0] == 'VIXCLS':
    del raw_vix[0]

# raw_total
raw_total.append(raw_date)
raw_total.append(raw_vix)
print("raw_tatle first line")
print(raw_total[0][0], raw_total[1][0])  # 2013-04-22 14.39

print(len(raw_date))  # 1304
print(len(raw_vix))  # 1304

print(dataCleaning.findIndexAtValue(raw_date, '2017-01-02')) # 965

# raw_vix의 문자열을 실수로. '.' 예외처리 필요.
raw_vix = dataCleaning.strToFloat(raw_vix,'.')
print(len(raw_vix))  # 1304

# 60일 이동평균선 그리기

drawGraph.drawAvgLine(raw_date,raw_vix,1200,1304,60)

# https://stackoverflow.com/questions/4805048/how-to-get-different-colored-lines-for-different-plots-in-a-single-figure

