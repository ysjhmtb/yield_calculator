import numpy as np
import matplotlib.pyplot as plt
import csv
import os




# rawX에서 targetValue의 인덱스 찾기
def findIndexAtValue(rawX, targetValue):
    for i in range(len(rawX)):
        if rawX[i] == targetValue:
            return i

# rawX의 문자열을 실수로. 비정형 문자열에 대한 예외처리 필요.
def strToFloat(rawX):
    floatX = []
    for i in range(len(rawX)):
        if rawX[i] != '.':
            floatX.append(float(rawX[i]))
        elif rawX[i] == '.':
            # 예외처리 문자열의 경우 0이 아니라 이전 인덱스의 값으로 대체.
            if i > 0:
                if rawX[i-1] == '.':
                    floatX.append(float(rawX[i-2]))
                else:
                    floatX.append(float(rawX[i - 1]))
            else:
                floatX.append(0)

    return floatX



# csv 파일 읽기
raw_date = []
raw_usd = []
raw_total = []

script_dir = os.path.dirname(__file__)
rel_path = "dataStorage/USDKRW0507.csv"
abs_file_path = os.path.join(script_dir,rel_path)

f = open(abs_file_path, 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    raw_date.append(line[0])
    raw_usd.append(line[1])
f.close()

if raw_date[0] == 'DATE':
    del raw_date[0]
if raw_usd[0] == 'DEXKOUS':
    del raw_usd[0]


# raw_total
raw_total.append(raw_date)
raw_total.append(raw_usd)


# raw_vix의 문자열을 실수로. '.' 예외처리 필요.
raw_usd = strToFloat(raw_usd)


print(findIndexAtValue(raw_date, '2015-01-01')) # 438
print(findIndexAtValue(raw_date, '2015-12-31')) # 698
print(findIndexAtValue(raw_date, '2018-04-27')) # 1304




# 9%
