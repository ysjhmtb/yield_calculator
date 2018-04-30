# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import csv


# 데이터 처리 클래스
class dataProcessing:
    def findIndexAtValue(self,raw_date,targetValue):
        for i in range(len(raw_date)):
            if raw_date[i] == targetValue:
                return i
    def strToFloat(self,raw_vix):
        float_vix = []
        for i in range(len(raw_vix)):
            if raw_vix[i] != '.':
                float_vix.append(float(raw_vix[i]))
            elif raw_vix[i] == '.':
                float_vix.append(0)
        return float_vix

proc = dataProcessing()


# csv 파일 읽기
raw_date = []
raw_vix = []

f = open('VIXCLS0414.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    raw_date.append(line[0])
    raw_vix.append(line[1])
f.close()


if raw_date[0]=='DATE':
    del raw_date[0]
if raw_vix[0]=='VIXCLS':
    del raw_vix[0]


print(len(raw_date))    # 1304
print(len(raw_vix))     # 1304

print(proc.findIndexAtValue(raw_date,'2017-01-02')) # 965


# raw_vix의 문자열을 실수로. '.' 예외처리 필요.
raw_vix = proc.strToFloat(raw_vix)
print(len(raw_vix))     # 1304


# 60일 이동평균선 그리기







# https://stackoverflow.com/questions/4805048/how-to-get-different-colored-lines-for-different-plots-in-a-single-figure


