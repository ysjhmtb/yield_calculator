import os
import csv
import matplotlib.pyplot as plt
import numpy as np

rawList = []

# 일자
date = []

# 종가
lastPrice = []

# 대비
dod = []

# NAV
nav = []

# 기초지수
kospi = []

# 거래량
tradeQunat = []

# 거래대금
tradeMoney = []

# 시가
startPrice = []

# 고가
highPrice = []

# 저가
lowPrice = []

# 인덱스
index = []

# 하나의 리스트에 통합.
rawList.append(date)
rawList.append(lastPrice)
rawList.append(dod)
rawList.append(nav)
rawList.append(kospi)
rawList.append(tradeQunat)
rawList.append(tradeMoney)
rawList.append(startPrice)
rawList.append(highPrice)
rawList.append(lowPrice)
rawList.append(index)

index = 0

# csv 파일 읽기 2017
script_dir = os.path.dirname(__file__)
rel_path = "dataStorage/leverage2017.csv"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, 'r', encoding='utf-8')

rdr = csv.reader(f)

for line in rdr:
    if line[0] == '일자' or line[1] == '종가' or line[2] == '대비' or \
            line[3] == 'NAV' or line[4] == '기초지수' or line[5] == '거래량' or \
            line[6] == '거래대금' or line[7] == '시가' or line[8] == '고가' or \
            line[9] == '저가':
        continue

    # 2017/12/28
    temp = line[0].replace("/", "")
    rawList[0].append(int(temp))

    # 17,650
    temp = line[1].replace(",", "")
    rawList[1].append(int(temp))

    # 450
    temp = line[2].replace(",", "")
    rawList[2].append(int(temp))

    # 17,770.66
    temp = line[3].replace(",", "")
    rawList[3].append(float(temp))

    # 324.74
    rawList[4].append(float(line[4]))

    # 10,110,980
    temp = line[5].replace(",", "")
    rawList[5].append(float(temp))

    # 176,703
    temp = line[6].replace(",", "")
    rawList[6].append(float(temp))

    # 17,225
    temp = line[7].replace(",", "")
    rawList[7].append(float(temp))

    # 17,650
    temp = line[8].replace(",", "")
    rawList[8].append(float(temp))

    # 17,220
    temp = line[9].replace(",", "")
    rawList[9].append(float(temp))

    rawList[10].append(index)
    index += 1

f.close()

# csv 파일 읽기 2018
script_dir = os.path.dirname(__file__)
rel_path = "dataStorage/leverage2018.csv"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, 'r', encoding='utf-8')

rdr = csv.reader(f)

for line in rdr:
    if line[0] == '일자' or line[1] == '종가' or line[2] == '대비' or \
            line[3] == 'NAV' or line[4] == '기초지수' or line[5] == '거래량' or \
            line[6] == '거래대금' or line[7] == '시가' or line[8] == '고가' or \
            line[9] == '저가':
        continue

    # 2017/12/28
    temp = line[0].replace("/", "")
    rawList[0].append(int(temp))

    # 17,650
    temp = line[1].replace(",", "")
    rawList[1].append(int(temp))

    # 450
    temp = line[2].replace(",", "")
    rawList[2].append(int(temp))

    # 17,770.66
    temp = line[3].replace(",", "")
    rawList[3].append(float(temp))

    # 324.74
    rawList[4].append(float(line[4]))

    # 10,110,980
    temp = line[5].replace(",", "")
    rawList[5].append(float(temp))

    # 176,703
    temp = line[6].replace(",", "")
    rawList[6].append(float(temp))

    # 17,225
    temp = line[7].replace(",", "")
    rawList[7].append(float(temp))

    # 17,650
    temp = line[8].replace(",", "")
    rawList[8].append(float(temp))

    # 17,220
    temp = line[9].replace(",", "")
    rawList[9].append(float(temp))

    rawList[10].append(index)
    index += 1

f.close()

tempLen = len(rawList[0])

'''
[
    0  : []
    1  : []
     ....
    10 : []
]
'''

print("test start")
for i in range(0, 11):
    print(rawList[i][tempLen - 1])

'''
test start
20180102
17800
150
17885.77
326.0
7913541.0
140634.0
17730.0
17880.0
176.0
337
'''

# 인덱스는 0 ~ 337
# 20 거래일 변동률
mom = []
for i in range(len(rawList[0])):
    if i < 20:
        mom.append(0)
        continue

    sPrice = rawList[1][i - 20]
    ePrice = rawList[1][i]
    temp = (ePrice - sPrice) / sPrice
    mom.append(temp)

rawList.append(mom)

# 길이 확인
print("len check")


def rawListLen(rawList):
    for i in range(len(rawList)):
        print(len(rawList[i]))


plt.plot(rawList[10], rawList[11])
plt.show()
